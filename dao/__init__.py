from util import DbUtil
from pojo import Book


class BookDao:
    bu: DbUtil

    def __init__(self):
        self.bu = DbUtil()

    def add_book(self, b: Book):
        try:
            assert isinstance(self.bu, DbUtil)
            # 只支持 %s 占位符
            # %s 支持任意类型
            self.bu.execute('insert into customer values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                            (b.CustomerId, b.Surname, b.CreditScore, b.Geography, b.Gender, b.Age, b.Tenure, b.Balance,
                             b.NumOfProducts, b.HasCrCard, b.IsActiveMember, b.EstimatedSalary, b.Exited))
            return '操作成功'
        except Exception as e:
            print(e)
            return '操作失败'

    def del_book(self, b: Book):
        try:
            assert isinstance(self.bu, DbUtil)
            # 只支持 %s 占位符
            # %s 支持任意类型
            self.bu.execute('delete from customer where CustomerId=%s',
                            (b.CustomerId))
            return '操作成功'
        except Exception as e:
            print(e)
            return '操作失败'

    def list_book(self, page: int = 1):
        self.bu = DbUtil()
        try:
            assert isinstance(self.bu, DbUtil)
            start = (page - 1) * 10
            rows = (page * 10000)
            return self.bu.execute_list('select * from customer limit %d,%d'
                                        % (start, rows))
        except Exception as e:
            print(e)
            return '操作失败'


if __name__ == "__main__":
    bd = BookDao()
    r = bd.list_book(page=3)
    print(r)

