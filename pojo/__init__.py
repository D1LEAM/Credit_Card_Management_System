# 实体类
# 新建pojo持久对象
class Book:  # 默认继承objject
    RowNumber: int
    CustomerId: int
    Surname: str
    CreditScore: int
    Geography: str
    Gender: str
    Age: int
    Tenure: int
    Balance: float
    NumOfProducts: int
    HasCrCard: int
    IsActiveMember: int
    EstimatedSalary: float
    Exited: int

    def __init__(self, RowNumber: int = None, CustomerId: int = None, Surname: str = None, Geography: str = None,
                 CreditScore: int = None, Gender: str = None, Age: int = None, Tenure: int = None, Balance: float = None,
                 NumOfProducts: int = None, HasCrCard: int = None, IsActiveMember: int = None, EstimatedSalary: float = None,
                 Exited: int = None):
        self.CustomerId = CustomerId
        self.RowNumber = RowNumber
        self.Surname = Surname
        self.CreditScore = CreditScore
        self.Geography = Geography
        self.Gender = Gender
        self.Age = Age
        self.Tenure = Tenure
        self.Balance = Balance
        self.NumOfProducts = NumOfProducts
        self.HasCrCard = HasCrCard
        self.IsActiveMember = IsActiveMember
        self.EstimatedSalary = EstimatedSalary
        self.Exited = Exited

    def __str__(self):
        return f"{self.CustomerId},{self.RowNumber},{self.Surname},{self.CreditScore},{self.Geography},{self.Gender}," \
               f"{self.Age},{self.Tenure},{self.Balance},{self.NumOfProducts},{self.HasCrCard},{self.IsActiveMember}," \
               f"{self.EstimatedSalary},{self.Exited}"


if __name__ == '__main__':
    b = Book(CustomerId=1)
    print(b)