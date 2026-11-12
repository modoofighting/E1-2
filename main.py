import json


class Quiz:
    """객관식 문제 하나를 나타냅니다."""

    def __init__(self, question, choices, answer):
        if len(choices) != 4:
            raise ValueError("선택지는 4개여야 합니다.")
        if not isinstance(question, str) or not question.strip():
            raise ValueError("문제는 비어 있지 않은 글자여야 합니다.")
        if not all(isinstance(choice, str) and choice.strip() for choice in choices):
            raise ValueError("선택지는 비어 있지 않은 글자여야 합니다.")
        if not isinstance(answer, int) or isinstance(answer, bool) or not 1 <= answer <= 4:
            raise ValueError("정답 번호는 1~4 사이의 정수여야 합니다.")

        self.question = question
        self.choices = choices
        self.answer = answer

    def show(self):
        print(self.question)
        for number, choice in enumerate(self.choices, start=1):
            print(f"{number}. {choice}")

    def check(self, user_answer):
        return user_answer == self.answer


default_quizzes = [
    Quiz(
        "Ubuntu Bash에서 현재 디렉터리 경로를 확인하는 명령어는?",
        ["ls", "pwd", "cd", "mkdir"],
        2,
    ),
    Quiz(
        "Docker 이미지로 새 컨테이너를 생성하고 실행하는 명령어는?",
        ["docker ps", "docker images", "docker run", "docker stop"],
        3,
    ),
    Quiz(
        "Dockerfile과 빌드 컨텍스트로 새 이미지를 만드는 명령어는?",
        ["docker build", "docker pull", "docker exec", "docker logs"],
        1,
    ),
    Quiz(
        "Git에서 준비한 변경을 로컬 커밋 이력으로 기록하는 명령어는?",
        ["git push", "git commit", "git add", "git status"],
        2,
    ),
    Quiz(
        "원격 GitHub 저장소를 새 로컬 폴더로 복제하는 명령어는?",
        ["git fetch", "git pull", "git checkout", "git clone"],
        4,
    ),
]


class QuizGame:
    def __init__(self):
        self.quizzes = default_quizzes.copy()
        self.best_score = 0
        self.has_played = False

    def show_menu(self):
        print("\n=== 코디세이 기술 탐험 퀴즈 ===")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 최고 점수 확인")
        print("5. 종료")

    def get_choice(self, minimum, maximum):
        while True:
            try:
                raw = input(f"{minimum}~{maximum} 중 번호를 입력하세요: ").strip()
            except (KeyboardInterrupt, EOFError):
                print("\n입력이 종료되었습니다.")
                return None

            if not raw:
                print("입력값이 없습니다. 다시 입력하세요.")
                continue
            try:
                choice = int(raw)
            except ValueError:
                print("숫자를 입력하세요.")
                continue
            if not minimum <= choice <= maximum:
                print(f"{minimum}~{maximum} 사이 숫자를 입력하세요.")
                continue
            return choice

    def play(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        correct_count = 0
        for quiz in self.quizzes:
            quiz.show()
            answer = self.get_choice(1, 4)
            if answer is None:
                return
            if quiz.check(answer):
                print("정답입니다!\n")
                correct_count += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.\n")

        score = round(correct_count / len(self.quizzes) * 100)
        print(f"결과: {correct_count}/{len(self.quizzes)}개 정답 ({score}점)")
        self.has_played = True
        if score > self.best_score:
            self.best_score = score
        self.save()

    def add_quiz(self):
        try:
            question = input("새 문제를 입력하세요: ").strip()
            if not question:
                print("문제 내용이 비어 있어 추가하지 않았습니다.")
                return
            choices = []
            for number in range(1, 5):
                choice = input(f"선택지 {number}을 입력하세요: ").strip()
                if not choice:
                    print("선택지가 비어 있어 추가하지 않았습니다.")
                    return
                choices.append(choice)
        except (KeyboardInterrupt, EOFError):
            print("\n입력이 취소되었습니다.")
            return

        answer = self.get_choice(1, 4)
        if answer is None:
            return
        self.quizzes.append(Quiz(question, choices, answer))
        self.save()
        print("퀴즈를 추가했습니다.")

    def show_list(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return
        print("\n=== 퀴즈 목록 ===")
        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"{number}. {quiz.question}")

    def show_score(self):
        if not self.has_played:
            print("아직 퀴즈를 푼 기록이 없습니다.")
            return
        print(f"최고 점수: {self.best_score}점 / 100점")

    def save(self):
        data = {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
            "has_played": self.has_played,
        }
        try:
            with open("state.json", "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
            print("진행 상황을 저장했습니다.")
        except OSError as error:
            print(f"파일을 저장하지 못했습니다: {error}")

    def load(self):
        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)
            loaded_quizzes = [
                Quiz(item["question"], item["choices"], item["answer"])
                for item in data["quizzes"]
            ]
            loaded_score = data["best_score"]
            if not isinstance(loaded_score, int) or isinstance(loaded_score, bool) or not 0 <= loaded_score <= 100:
                raise ValueError("최고 점수 데이터가 올바르지 않습니다.")
            has_played = data.get("has_played", loaded_score > 0)
            if not isinstance(has_played, bool):
                raise ValueError("플레이 기록 데이터가 올바르지 않습니다.")
            if "has_played" not in data and loaded_quizzes and 0 < loaded_score <= len(loaded_quizzes):
                loaded_score = round(loaded_score / len(loaded_quizzes) * 100)
            self.quizzes = loaded_quizzes
            self.best_score = loaded_score
            self.has_played = has_played
            print("저장된 퀴즈를 불러왔습니다.")
        except FileNotFoundError:
            self.quizzes = default_quizzes.copy()
            self.best_score = 0
            self.has_played = False
            print("저장 파일이 없어 기본 퀴즈로 시작합니다.")
        except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
            self.quizzes = default_quizzes.copy()
            self.best_score = 0
            self.has_played = False
            print(f"저장 파일을 읽지 못해 기본 퀴즈로 시작합니다: {error}")

    def run(self):
        while True:
            self.show_menu()
            choice = self.get_choice(1, 5)
            if choice is None:
                self.save()
                print("게임을 종료합니다.")
                break

            if choice == 1:
                self.play()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.show_list()
            elif choice == 4:
                self.show_score()
            else:
                self.save()
                print("게임을 종료합니다.")
                break


if __name__ == "__main__":
    game = QuizGame()
    game.load()
    game.run()
