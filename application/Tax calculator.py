class CalcTax:
    MIN_LIMIT = 250000
    FIVE_LIMIT = 500000
    TEN_LIMIT = 1000000

    FIRST_RATE = 5
    SECOND_RATE = 20
    THIRD_RATE = 30

    FIRST_SLAB_TAX = MIN_LIMIT * FIRST_RATE / 100
    SECOND_SLAB_TAX = FIVE_LIMIT * SECOND_RATE / 100

    def __init__(self, total_income, saving=0, hra=0):
        self.total_income = total_income
        self.saving = saving
        self.hra = hra

    def calculate_tax(self):
        taxable_income = self.total_income - self.hra - self.saving

        if taxable_income < 0:
            taxable_income = 0
        print("Taxable income is", taxable_income)

        if taxable_income <= CalcTax.MIN_LIMIT:
            return 0

        elif taxable_income > CalcTax.TEN_LIMIT:
            tax = CalcTax.FIRST_SLAB_TAX \
                  + CalcTax.SECOND_SLAB_TAX \
                  + (taxable_income - CalcTax.TEN_LIMIT) * CalcTax.THIRD_RATE / 100

        elif taxable_income > CalcTax.FIVE_LIMIT:
            tax = CalcTax.FIRST_SLAB_TAX \
                  + (taxable_income - CalcTax.FIVE_LIMIT) * CalcTax.SECOND_RATE / 100

        else:
            tax = (taxable_income - CalcTax.MIN_LIMIT) * CalcTax.FIRST_RATE / 100

        return tax


ctc = int(input("Enter your CTC: "))
saving = int(input("Enter your Savings: "))
hra = int(input("Enter your HRA : "))
taxCalc = CalcTax(ctc, saving, hra)
print(taxCalc.calculate_tax())
