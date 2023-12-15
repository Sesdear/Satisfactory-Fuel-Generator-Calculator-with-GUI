import customtkinter
import json
import math


class Entry(customtkinter.CTkEntry):
    def __init__(self, master):
        super().__init__(master, placeholder_text="MW", width=90, height=32)
        self.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

    def get_value(self):
        entry_text = self.get()
        if entry_text.strip():
            entry_get = int(entry_text)
            return entry_get
        else:
            return 0

class CheckBoxFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.title = customtkinter.CTkLabel(self, text="Rare oil", fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")
        self.checkbox_1 = customtkinter.CTkCheckBox(self, text="Impure")
        self.checkbox_1.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox_2 = customtkinter.CTkCheckBox(self, text="Normal")
        self.checkbox_2.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox_3 = customtkinter.CTkCheckBox(self, text="Pure")
        self.checkbox_3.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="w")

    def get_checked_boxes_count(self):
        count = 0
        if self.checkbox_1.get() == 1:
            count += 1
        if self.checkbox_2.get() == 1:
            count += 1
        if self.checkbox_3.get() == 1:
            count += 1
        return count

def energy_gen_calc(input_user_energy):
    with open("fuel_gen_val.json") as json_file:
        energy_gen_need_output = json.load(json_file)
    token = energy_gen_need_output["MW"]
    calc_ener = math.ceil(input_user_energy / token)
    json_file.close()
    return calc_ener

def gen_need_fuel(input_user_energy):
    with open("fuel_gen_val.json") as json_file:
        fuel_per_min = json.load(json_file)
    token_one = fuel_per_min["MW"]
    token_two = fuel_per_min["fuel_per_min"]
    calc_ener = input_user_energy / token_one
    calc_fuel = calc_ener * token_two
    json_file.close()
    return calc_fuel

def materials_need_gen(input_user_energy):
    with open("fuel_gen_val.json") as json_file:
        gen_need_materials = json.load(json_file)
    token_energy = gen_need_materials["MW"]
    token_one = gen_need_materials["Computers"]
    token_two = gen_need_materials["Heavy_Modular_Frame"]
    token_three = gen_need_materials["Rotors"]
    token_four = gen_need_materials["Rubber"]
    token_five = gen_need_materials["Quickwire"]
    calc_ener = input_user_energy / token_energy
    calc_computers = calc_ener * token_one
    calc_heavy_modular = calc_ener * token_two
    calc_rotors = calc_ener * token_three
    calc_rubber = calc_ener * token_four
    calc_quickwire = calc_ener * token_five

    fin_result = print('You need to build Fuel generators:',
                       math.ceil(calc_computers), '-Computers;',
                       math.ceil(calc_heavy_modular), '-Heavy Modulars Frame;',
                       math.ceil(calc_rotors), '-Rotors;',
                       math.ceil(calc_rubber), '-Rubbers;',
                       math.ceil(calc_quickwire), '-Quickwire')
    json_file.close()
    return fin_result

def refinery(input_user_energy):
    with open("refinery_val.json") as json_file:
        refinery_values = json.load(json_file)
    with open("fuel_gen_val.json") as json_file1:
        fuel_gen_values = json.load(json_file1)
    token_energy = fuel_gen_values["MW"]
    calc_ener = input_user_energy / token_energy
    ref_fuel_output = refinery_values["fuel_ouptut_permin"]
    gen_fuel_values = fuel_gen_values["fuel_per_min"]
    calc_gen = gen_fuel_values * calc_ener
    result_ref = calc_gen / ref_fuel_output
    json_file.close()
    json_file1.close()
    return result_ref

def oil_extract(input_user_energy, input_rare_of_oil):
    with open("oil_ext_val.json") as json_file:
        oil_extra_val = json.load(json_file)
    with open("refinery_val.json") as json_file1:
        refinery_val = json.load(json_file1)
    with open("fuel_gen_val.json") as json_file2:
        fuel_gen = json.load(json_file2)
    token_energy = fuel_gen["MW"]
    calc_ener = input_user_energy / token_energy
    ref_fuel_output = refinery_val["fuel_ouptut_permin"]
    gen_fuel_values = fuel_gen["fuel_per_min"]
    calc_gen = gen_fuel_values * calc_ener
    result_ref = calc_gen / ref_fuel_output
    refinery = refinery_val["need_oil_Fuel_processing_permin"]
    res = result_ref * refinery

    if input_rare_of_oil == 1:
        oil_1 = oil_extra_val["impure"]
        oil_result = res / oil_1
    elif input_rare_of_oil == 2:
        oil_2 = oil_extra_val["normal"]
        oil_result = res / oil_2
    elif input_rare_of_oil == 3:
        oil_3 = oil_extra_val["pure"]
        oil_result = res / oil_3
    return oil_result
