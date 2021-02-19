from decimal import Decimal


class CommissionEmployee:
    def __init__(self, first_name, last_name, ssn, gross_sales, commission_rate):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__ssn = ssn
        self.__gross_sales = gross_sales
        self.__commission_rate = commission_rate

    @property
    def firs_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def ssn(self):
        return self.__ssn

    @property
    def commission_rate(self):
        return self.__commission_rate

    @property
    def gross_sales(self):
        return self.__gross_sales

    @commission_rate.setter
    def commission_rate(self, rate):
        if not (Decimal('0.0') < rate < Decimal('1.0')):
            raise ValueError('Interest rate must be grater than 0 and less than 1')
        self.__commission_rate = rate

    def earnings(self):
        return self.gross_sales * self.commission_rate

    def __repr__(self):
        return ('Commission Employee: ' +
                f'{self.firs_name} {self.last_name}\n' +
                f'social security number: {self.ssn}\n' +
                f'gross sales: {self.gross_sales:.2f}\n' +
                f'commission rate: {self.commission_rate:.2f}')


def main():
    employee = CommissionEmployee('Sue', 'Jones', '333-33-3333', Decimal('10000.00'), Decimal('0.06'))
    print(employee)


main()
