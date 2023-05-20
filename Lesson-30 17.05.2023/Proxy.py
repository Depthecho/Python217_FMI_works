# Теоретически ресурсоемкий объект
class College:
    def studyingInCollege(self):
        print("Studying In College....")

# Относительно менее ресурсоемкий прокси,
# выступающий в роли посредника.
# Создает экземпляр объекта College только
# в том случае, если было оплачено обучение.


class CollegeProxy:
    def __init__(self):
        self.feeBalance = 1000
        self.college = None

    def studyingInCollege(self):
        print("Proxy in action. Checking to see if the balance "
              "of student is clear or not...")
        if self.feeBalance <= 500:
            # Если баланс меньше 500, пускаем ученика
            # в колледж и позволяем учиться
            self.college = College()
            self.college.studyingInCollege()
        else:
            # В противном случае не пускаем ученика в колледж
            print("Your fee balance is greater than 500, first pay the fee")


# Создаём прокси
collegeProxy = CollegeProxy()

# Студент пытается учиться в Колледже с балансом по умолчанию 1000.
# Поскольку он логически не может учиться с балансом в 1000
# то нет смысла создавать объект Колледжа
collegeProxy.studyingInCollege()

# Меняем баланс студента, чтобы он смог учиться в Колледже
collegeProxy.feeBalance = 100

# Студент пытается учиться в Колледже с балансом в 100. Должно сработать
collegeProxy.studyingInCollege()
