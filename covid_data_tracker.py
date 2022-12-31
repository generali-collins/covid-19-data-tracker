import tkinter

import customtkinter
from covid_data import *

customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('Patriots | COVID-19 Data Tracker')
        self.geometry('920x390')
        self.protocol('WM_DELETE_WINDOW', self.close_app)
        self.bind('<Q>', self.close_app)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self, width=400, corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)

        self.frame_left.grid_rowconfigure(0, minsize=10)

        self.title_label = customtkinter.CTkLabel(master=self.frame_left,
                                                  text="COVID-19 Tracker",
                                                  text_font=("Roboto Medium", -16))
        self.title_label.grid(row=1, column=0, pady=10, padx=10)

        self.country_entry_prompt = customtkinter.CTkLabel(self.frame_left, text="Country", anchor="w")
        self.country_entry_prompt.grid(row=2, column=0, pady=(10, 0), padx=20)

        self.country_entry = customtkinter.CTkEntry(master=self.frame_left, placeholder_text="Enter country")
        self.country_entry.grid(row=3, column=0, pady=(5, 10), padx=20)

        self.are_travelling = 0
        self.travelling_var = tkinter.IntVar(value=0)
        self.travelling_prompt = customtkinter.CTkLabel(self.frame_left, text="Are you Travelling?", anchor="w")
        self.travelling_prompt.grid(row=4, column=0, pady=(10, 0), padx=20)

        self.travelling_yes = customtkinter.CTkRadioButton(master=self.frame_left,
                                                           variable=self.travelling_var,
                                                           text="Yes",
                                                           value=0,
                                                           command=self.set_travelling_yes)
        self.travelling_yes.grid(row=5, column=0, pady=10, padx=20, sticky="wn")

        self.travelling_no = customtkinter.CTkRadioButton(master=self.frame_left,
                                                           variable=self.travelling_var,
                                                           text="No",
                                                           value=1,
                                                          command=self.set_travelling_no)
        self.travelling_no.grid(row=6, column=0, pady=10, padx=20, sticky="wn")

        self.country2_entry_prompt = customtkinter.CTkLabel(self.frame_left, text="Destination Country", anchor="w")
        self.country2_entry_prompt.grid(row=7, column=0, pady=(10, 0), padx=20)

        self.country2_entry = customtkinter.CTkEntry(master=self.frame_left, placeholder_text="Enter country")
        self.country2_entry.grid(row=8, column=0, pady=(5, 10), padx=20)

        self.get_results_button = customtkinter.CTkButton(master=self.frame_left,
                                                          text="Get Results",
                                                          command=self.get_results)
        self.get_results_button.grid(row=9, column=0, pady=0, padx=20)

        # ===================== right_side ====================
        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure((0,1), weight=2)

        self.country_output_label = customtkinter.CTkLabel(master=self.frame_info, text="Country")
        self.country_output_label.grid(column=0, row=0, sticky="nwe", padx=10, pady=10)

        self.country_output_grid = customtkinter.CTkFrame(master=self.frame_info)
        self.country_output_grid.grid(column=1, row=0, sticky="nwe", padx=10, pady=10)

        self.country_output = customtkinter.CTkLabel(master=self.country_output_grid, text='0')
        self.country_output.grid(column=0, row=0)

        self.total_cases_output_label = customtkinter.CTkLabel(master=self.frame_info, text="Total Cases")
        self.total_cases_output_label.grid(column=0, row=1, sticky="nwe", padx=10, pady=10)

        self.total_cases_output_grid = customtkinter.CTkFrame(master=self.frame_info)
        self.total_cases_output_grid.grid(column=1, row=1, sticky="nwe", padx=10, pady=10)

        self.total_cases_output = customtkinter.CTkLabel(master=self.total_cases_output_grid, text='0')
        self.total_cases_output.grid(column=0, row=0)

        self.today_cases_output_label = customtkinter.CTkLabel(master=self.frame_info, text="Today's Cases")
        self.today_cases_output_label.grid(column=0, row=2, sticky="nwe", padx=10, pady=10)

        self.today_cases_output_grid = customtkinter.CTkFrame(master=self.frame_info)
        self.today_cases_output_grid.grid(column=1, row=2, sticky="nwe", padx=10, pady=10)

        self.today_cases_output = customtkinter.CTkLabel(master=self.today_cases_output_grid, text='0')
        self.today_cases_output.grid(column=0, row=0)

        self.recovered_output_label = customtkinter.CTkLabel(master=self.frame_info, text="Recovered")
        self.recovered_output_label.grid(column=0, row=3, sticky="nwe", padx=10, pady=10)

        self.recovered_output_grid = customtkinter.CTkFrame(master=self.frame_info)
        self.recovered_output_grid.grid(column=1, row=3, sticky="nwe", padx=10, pady=10)

        self.recovered_output = customtkinter.CTkLabel(master=self.recovered_output_grid, text='0')
        self.recovered_output.grid(column=0, row=0)

        self.deaths_output_label = customtkinter.CTkLabel(master=self.frame_info, text="Deaths")
        self.deaths_output_label.grid(column=0, row=4, sticky="nwe", padx=10, pady=10)

        self.deaths_output_grid = customtkinter.CTkFrame(master=self.frame_info)
        self.deaths_output_grid.grid(column=1, row=4, sticky="nwe", padx=10, pady=10)

        self.deaths_output = customtkinter.CTkLabel(master=self.deaths_output_grid, text='0')
        self.deaths_output.grid(column=0, row=0)

        self.status_output_label = customtkinter.CTkLabel(master=self.frame_info, text="Status")
        self.status_output_label.grid(column=0, row=5, sticky="nwe", padx=10, pady=10)

        self.status_output_grid = customtkinter.CTkFrame(master=self.frame_info)
        self.status_output_grid.grid(column=1, row=5, sticky="nwe", padx=10, pady=10)

        self.status_output = customtkinter.CTkLabel(master=self.status_output_grid, text='0')
        self.status_output.grid(column=0, row=0)

        # ====== second section ====== #
        self.frame_info2 = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info2.grid(row=0, column=3, columnspan=2, rowspan=4, pady=20, padx=20)
        self.frame_info2.rowconfigure(0, weight=1)
        self.frame_info2.columnconfigure((0, 1), weight=2)

        self.country_output_label2 = customtkinter.CTkLabel(master=self.frame_info2, text="Country")
        self.country_output_label2.grid(column=0, row=0, sticky="nwe", padx=10, pady=10)

        self.country_output_grid2 = customtkinter.CTkFrame(master=self.frame_info2)
        self.country_output_grid2.grid(column=1, row=0, sticky="nwe", padx=10, pady=10)

        self.country_output2 = customtkinter.CTkLabel(master=self.country_output_grid2, text='0')
        self.country_output2.grid(column=0, row=0)

        self.total_cases_output_label2 = customtkinter.CTkLabel(master=self.frame_info2, text="Total Cases")
        self.total_cases_output_label2.grid(column=0, row=1, sticky="nwe", padx=10, pady=10)

        self.total_cases_output_grid2 = customtkinter.CTkFrame(master=self.frame_info2)
        self.total_cases_output_grid2.grid(column=1, row=1, sticky="nwe", padx=10, pady=10)

        self.total_cases_output2 = customtkinter.CTkLabel(master=self.total_cases_output_grid2, text='0')
        self.total_cases_output2.grid(column=0, row=0)

        self.today_cases_output_label2 = customtkinter.CTkLabel(master=self.frame_info2, text="Today's Cases")
        self.today_cases_output_label2.grid(column=0, row=2, sticky="nwe", padx=10, pady=10)

        self.today_cases_output_grid2 = customtkinter.CTkFrame(master=self.frame_info2)
        self.today_cases_output_grid2.grid(column=1, row=2, sticky="nwe", padx=10, pady=10)

        self.today_cases_output2 = customtkinter.CTkLabel(master=self.today_cases_output_grid2, text='0')
        self.today_cases_output2.grid(column=0, row=0)

        self.recovered_output_label2 = customtkinter.CTkLabel(master=self.frame_info2, text="Recovered")
        self.recovered_output_label2.grid(column=0, row=3, sticky="nwe", padx=10, pady=10)

        self.recovered_output_grid2 = customtkinter.CTkFrame(master=self.frame_info2)
        self.recovered_output_grid2.grid(column=1, row=3, sticky="nwe", padx=10, pady=10)

        self.recovered_output2 = customtkinter.CTkLabel(master=self.recovered_output_grid2, text='0')
        self.recovered_output2.grid(column=0, row=0)

        self.deaths_output_label2 = customtkinter.CTkLabel(master=self.frame_info2, text="Deaths")
        self.deaths_output_label2.grid(column=0, row=4, sticky="nwe", padx=10, pady=10)

        self.deaths_output_grid2 = customtkinter.CTkFrame(master=self.frame_info2)
        self.deaths_output_grid2.grid(column=1, row=4, sticky="nwe", padx=10, pady=10)

        self.deaths_output2 = customtkinter.CTkLabel(master=self.deaths_output_grid2, text='0')
        self.deaths_output2.grid(column=0, row=0)

        self.status_output_label2 = customtkinter.CTkLabel(master=self.frame_info2, text="Status")
        self.status_output_label2.grid(column=0, row=5, sticky="nwe", padx=10, pady=10)

        self.status_output_grid2 = customtkinter.CTkFrame(master=self.frame_info2)
        self.status_output_grid2.grid(column=1, row=5, sticky="nwe", padx=10, pady=10)

        self.status_output2 = customtkinter.CTkLabel(master=self.status_output_grid2, text='0')
        self.status_output2.grid(column=0, row=0)
        # ============================ #

        self.travelling_no.select()


    def set_travelling_yes(self):
        self.are_travelling = 1

    def set_travelling_no(self):
        self.are_travelling = 0

    def get_results(self):
        print('Button Pressed')
        country_name = self.country_entry.get()
        country = CovidData(country_name)
        self.country_output.configure(text=(country.get_country_name()))
        self.total_cases_output.configure(text=('{:,}'.format(country.get_cases())))
        self.today_cases_output.configure(text=('{:,}'.format(country.get_cases_today())))
        self.recovered_output.configure(text=('{:,}'.format(country.get_recovered())))
        self.deaths_output.configure(text=('{:,}'.format(country.get_deaths())))

        safety_index = country.get_cases_today()
        if safety_index == 0:
            self.status_output.configure(text='SAFE', text_color="green")
        else:
            self.status_output.configure(text='UNSAFE', text_color="red")

        if self.are_travelling == 1:
            country_name2 = self.country2_entry.get()
            country2 = CovidData(country_name2)
            self.country_output2.configure(text=(country2.get_country_name()))
            self.total_cases_output2.configure(text=('{:,}'.format(country2.get_cases())))
            self.today_cases_output2.configure(text=('{:,}'.format(country2.get_cases_today())))
            self.recovered_output2.configure(text=('{:,}'.format(country2.get_recovered())))
            self.deaths_output2.configure(text=('{:,}'.format(country2.get_deaths())))

            safety_index2 = country2.get_cases_today()
            if safety_index2 == 0:
                self.status_output2.configure(text='SAFE', text_color="green")
            else:
                self.status_output2.configure(text='UNSAFE', text_color="red")
            pass
        else:
            self.country_output2.configure(text="n/a")
            self.total_cases_output2.configure(text="n/a")
            self.today_cases_output2.configure(text="n/a")
            self.recovered_output2.configure(text="n/a")
            self.deaths_output2.configure(text="n/a")
            self.status_output2.configure(text="n/a")

    def start(self):
        self.mainloop()

    def close_app(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.start()