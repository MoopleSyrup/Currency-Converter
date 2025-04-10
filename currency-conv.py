""" import tkinter as tk
from forex_python.converter import CurrencyRates

common_currencies = ['USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD', 'AUD', 'NZD']

class CurrencyConverter:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('CurrencyConverter')
        self.root.geometry('200x180')

        self.from_var = tk.StringVar(self.root)
        self.from_var.set('USD')
        self.from_menu = tk.OptionMenu(self.root, self.from_var, *common_currencies)
        self.from_menu.pack(pady=1)

        self.to_var = tk.StringVar(self.root)
        self.to_var.set('EUR')
        self.to_menu = tk.OptionMenu(self.root, self.to_var, *common_currencies)
        self.to_menu.pack(pady=1)

        self.amount_label = tk.Label(self.root, text='Amount: ')
        self.amount_label.pack(pady=1)

        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack(pady=1)

        self.convert_button = tk.Button(self.root, text='Convert', command=self.convert_currency)
        self.convert_button.pack(pady=1)

        self.result_label = tk.Label(self.root, text='')
        self.result_label.pack(pady=1)

        self.root.mainloop()


    def convert_currency(self):
        try:
            from_currency = self.from_var.get()
            to_currency = self.to_var.get()
            amount = float(self.amount_entry.get())

            c_rates = CurrencyRates()

            rate = c_rates.get_rate(from_currency, to_currency)
            converted_amount = amount * rate

            self.result_label.config(text=f'{amount} {from_currency} = {converted_amount:.2f} {to_currency}')
        except ValueError:
            self.result_label.config(text='Please enter a valid number!')
        except Exception:
            self.result_label.config(text='Error Occured!')

if __name__ == '__main__':
    CurrencyConverter() """








import tkinter as tk
from forex_python.converter import CurrencyRates

common_currencies = ['USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD', 'NZD']

class CurrencyConverter:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Currency Converter')
        self.root.geometry('250x220')

        self.from_var = tk.StringVar(self.root)
        self.from_var.set('USD')
        self.from_menu = tk.OptionMenu(self.root, self.from_var, *common_currencies)
        self.from_menu.pack(pady=5)

        self.to_var = tk.StringVar(self.root)
        self.to_var.set('EUR')
        self.to_menu = tk.OptionMenu(self.root, self.to_var, *common_currencies)
        self.to_menu.pack(pady=5)

        self.amount_label = tk.Label(self.root, text='Amount:')
        self.amount_label.pack()

        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack(pady=5)

        self.convert_button = tk.Button(self.root, text='Convert', command=self.convert_currency)
        self.convert_button.pack(pady=5)

        self.result_label = tk.Label(self.root, text='', font=('Arial', 10, 'bold'))
        self.result_label.pack(pady=10)

        self.root.mainloop()

    def convert_currency(self):
        try:
            from_currency = self.from_var.get()
            to_currency = self.to_var.get()
            amount = float(self.amount_entry.get().strip())

            c_rates = CurrencyRates()
            rate = c_rates.get_rate(from_currency, to_currency)
            converted_amount = amount * rate

            self.result_label.config(
                text=f'{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}'
            )
        except ValueError as ve:
            print("ValueError:", ve)
            self.result_label.config(text='Please enter a valid number!')
        except Exception as e:
            print("Exception:", e)
            self.result_label.config(text='Something went wrong!')


        print(f"User input: '{self.amount_entry.get()}'")


if __name__ == '__main__':
    CurrencyConverter()


