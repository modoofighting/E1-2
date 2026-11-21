import json
import os
import random
import tempfile
from pathlib import Path
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def show(self):
        print(self.question)
        for number, choice in enumerate(self.choices, start=1):
            print(f"{number}, {choice}")

    def check(self, user_answer):
        return user_answer == self.answer  

# main.py와 같은 폴더에 저장
STATE_PATH = Path(__file__).with_name("state.json")


def load_state(default_quizzes):
    """저장 파일을 읽고 (퀴즈, 최고 점수, 저장 가능 여부)를 돌려준다."""
    try:
        with STATE_PATH.open("r", encoding="utf-8") as file:
            data = json.load(file)

        saved_quizzes = data["quizzes"]
        saved_score = data["best_score"]
        if not isinstance(saved_quizzes, list):
            raise ValueError("퀴즈 목록 형식이 올바르지 않습니다.")
        if saved_score is not None and (
            type(saved_score) not in (int, float) or not 0 <= saved_score <= 100
        ):
            raise ValueError("최고 점수 형식이 올바르지 않습니다.")

        loaded_quizzes = []
        for item in saved_quizzes:
            question = item["question"]
            choices = item["choices"]
            answer = item["answer"]
            if (
                not isinstance(question, str) or not question.strip()
                or not isinstance(choices, list) or len(choices) != 4
                or any(not isinstance(choice, str) or not choice.strip() for choice in choices)
                or type(answer) is not int or not 1 <= answer <= 4
            ):
                raise ValueError("퀴즈 형식이 올바르지 않습니다.")
            loaded_quizzes.append(Quiz(question, choices, answer))

        print(f"저장된 퀴즈 {len(loaded_quizzes)}개를 불러왔습니다.")
        return loaded_quizzes, saved_score, True

    except FileNotFoundError:
        print("저장 파일이 없어 기본 퀴즈로 시작합니다.")
        return default_quizzes, None, True

    except (OSError, ValueError, KeyError, TypeError):
        print("저장 파일을 읽을 수 없어 기본 퀴즈로 시작합니다.")
        print("기존 파일을 보호하기 위해 이번 실행에서는 저장하지 않습니다.")
        return default_quizzes, None, False


def save_state(quizzes, best_score):
    """임시 파일에 먼저 쓴 다음 저장 파일을 교체한다."""
    data = {
        "quizzes": [
            {"question": quiz.question, "choices": quiz.choices, "answer": quiz.answer}
            for quiz in quizzes
        ],
        "best_score": best_score,
    }
    temp_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=STATE_PATH.parent,
            prefix=".state-", suffix=".tmp", delete=False,
        ) as file:
            temp_path = Path(file.name)
            json.dump(data, file, ensure_ascii=False, indent=2)
        os.replace(temp_path, STATE_PATH)
        print("퀴즈와 최고 점수를 저장했습니다.")
    except OSError:
        print("저장 파일에 기록하지 못했습니다.")
    finally:
        if temp_path is not None:
            try:
                temp_path.unlink(missing_ok=True)
            except OSError:
                print("임시 파일을 정리하지 못했습니다.")

class QuizGame:
    def __init__(self, default_quizzes):
        self.quizzes, self.best_score, self.can_save = load_state(default_quizzes)

    def show_menu(self):
        print("=" * 40)
        print("       코디세이 기술 탐험 퀴즈")
        print("=" * 40)
        print("1. 퀴즈풀기")
        print("2. 퀴즈추가")
        print("3. 퀴즈 목록")
        print("4. 최고 점수 확인")
        print("5. 종료")
        print("=" * 40)

    def get_answer(self):
        while True:
            answer = input("정답 번호를 입력하세요: ").strip()
            if answer in ["1", "2", "3", "4"]:
                return int(answer)
            print("1부터 4까지의 번호를 입력하세요.")

    def play(self):
        print("퀴즈 풀기를 선택했습니다")

        if not self.quizzes:
            print("등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요.")
            return

        correct_count = 0
        quiz_order = self.quizzes.copy()
        random.shuffle(quiz_order)

        for quiz in quiz_order:
            quiz.show()

            user_answer = self.get_answer()

            if quiz.check(user_answer):
                print("정답입니다.")
                correct_count += 1
            else:
                print("오답입니다.")

        print("퀴즈가 끝났습니다.")
        print("맞힌 문제 수:", correct_count)

        score = round(correct_count / len(self.quizzes) * 100)  
        print(f"점수: {score}%")

        if self.best_score is None or score > self.best_score:
            self.best_score = score
        self.save_if_allowed()


    def add_quiz(self):
        print("퀴즈 추가를 선택했습니다")
        while True:
            question = input("새 문제를 입력하세요: ").strip()

            if question:
                break

            print("문제를 입력해 주세요.")
        print("입력한 문제:", question)

        choices = []

        for number in range(1, 5):
            while True:
                choice_text = input(f"선택지 {number}: ").strip()

                if choice_text:
                    break

                print("선택지를 입력해 주세요.")

            choices.append(choice_text)
        print("입력한 선택지:", choices)
        answer = self.get_answer()

        print("입력한 정답 번호:", answer) 
        new_quiz = Quiz(question, choices, answer)
        print("새 퀴즈:", new_quiz.question)
        self.quizzes.append(new_quiz)
        print("전체 퀴즈 개수:", len(self.quizzes))
        self.save_if_allowed()


    def show_list(self):
        print("=" * 40)
        print("       등록된 퀴즈 목록")
        print("=" * 40)

        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
        else:
            for number, quiz in enumerate(self.quizzes, start=1):
                print(f"{number}. {quiz.question}")

    def show_best_score(self):
        if self.best_score is None:
            print("아직 완료한 퀴즈가 없습니다.")
        else:
            print(f"최고 점수: {self.best_score}%")


    def save_if_allowed(self):
        if self.can_save:
            save_state(self.quizzes, self.best_score)
        else:
            print("기존 저장 파일을 보호하기 위해 저장을 건너뜁니다.")

    def run(self):
        while True:
            self.show_menu()

            choice = input("메뉴 번호를 선택하세요: ").strip()

            if choice == "1":
                self.play()

            elif choice == "2":
                self.add_quiz()

            elif choice == "3":
                self.show_list()

            elif choice == "4":
                self.show_best_score()

            elif choice == "5":
                self.save_if_allowed()
                print("종료합니다")
                break
            else:
                print("1부터 5까지의 번호를 입력하세요")


quiz1 = Quiz(
    "현재 디렉터리 경로를 확인하는 명령어는?",
    ["ls", "pwd", "cd", "mkdir"],
    2,  
)
quiz2 = Quiz(
    "Docker 이미지로 새 컨테이너를 실행하는 명령어는?",
    ["docker run", "docker build", "docker ps", "docker stop"],         
    1,
)
quiz3 = Quiz(
    "Dockerfile로 이미지를 만드는 명령어는?",
    ["docker run", "docker build", "docker ps", "docker stop"],
    2,
)
quiz4 = Quiz(
    "Git에서 준비한 변경을 로컬 이력으로 기록하는 명령어는?",
    ["git push", "git commit", "git add", "git status"],
    2,
)
quiz5 = Quiz(   
    "현재 Git 저장소의 변경 상태를 확인하는 명령어는?",
    ["git status", "git push", "git commit", "git clone"],
    1,
)

default_quizzes = [quiz1, quiz2, quiz3, quiz4, quiz5]
game = QuizGame(default_quizzes)
print("퀴즈 개수:", len(game.quizzes))
if game.quizzes:
    print("첫 번째 퀴즈:", game.quizzes[0].question)



try:
    game.run()
except KeyboardInterrupt:
    print("\n게임을 중단했습니다.")
    game.save_if_allowed()
except EOFError:
    print("\n입력이 종료되어 게임을 마칩니다.")
    game.save_if_allowed()
