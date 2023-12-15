import customtkinter
from helper_functions import Entry, CheckBoxFrame, energy_gen_calc, gen_need_fuel, refinery, oil_extract

class App(customtkinter.CTk):
    def __init__(self, master):
        super().__init__(master)

        self.theme = customtkinter.set_default_color_theme("dark-blue")

        self.title("FuelGenCalculator")
        self.geometry("600x250")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.entry_1 = Entry(self)
        self.entry_1.grid(row=0, column=0, padx=10, pady=10, sticky="nsw")

        self.checkbox_frame = CheckBoxFrame(self)
        self.checkbox_frame.grid(row=1, column=0, padx=10, pady=11, sticky="nsw")

        self.label_gen = customtkinter.CTkLabel(self, text="Fuel Gen Need", height=10, width=50, font=("Brass Mono", 15, "bold"))
        self.label_gen.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        self.label_fuel = customtkinter.CTkLabel(self, text="Fuel per/min", height=10, width=50, font=("Brass Mono", 15, "bold"))
        self.label_fuel.grid(row=0, column=2, padx=10, pady=10, sticky="e")

        self.label_ref = customtkinter.CTkLabel(self, text="Refineries", height=10, width=50, font=("Brass Mono", 15, "bold"))
        self.label_ref.grid(row=0, column=3, padx=10, pady=10, sticky="e")

        self.label_oil_ext = customtkinter.CTkLabel(self, text="Oil Extractors", height=10, width=50, font=("Brass Mono", 15, "bold"))
        self.label_oil_ext.grid(row=0, column=4, padx=10, pady=10, sticky="e")

        self.button = customtkinter.CTkButton(self, text="Calculate", command=self.button_callback)
        self.button.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    def button_callback(self):
        input_user_energy = self.entry_1.get_value()
        input_rare_of_oil = self.checkbox_frame.get_checked_boxes_count()

        self.label_gen.configure(text="Fuel Gen Need \n" + str(energy_gen_calc(input_user_energy)))
        self.label_fuel.configure(text="Fuel per/min \n" + str(gen_need_fuel(input_user_energy)))
        self.label_ref.configure(text="Refineries \n" + str(refinery(input_user_energy)))
        self.label_oil_ext.configure(text="Oil Extractors \n" + str(oil_extract(input_user_energy, input_rare_of_oil)))

if __name__ == "__main__":
    app = App(None)
    app.mainloop()
