from kivy.app import App
from kivy.properties import ObjectProperty
from kivymd.uix.pickers import MDDatePicker

from kivy.uix.screenmanager import Screen
from modules.datamanager import SchoolCalendar
from modules.msgmanager import show_toast


class CalendarScreen(Screen):
    year = ObjectProperty()
    
    def __init__(self, **kwargs):
        super(CalendarScreen, self).__init__(**kwargs)
        
    def on_pre_enter(self):
        calendas = []
        
        sch_calendas = SchoolCalendar()
        
        for cal in sch_calendas.get_schcalendars():
            calendas.append(cal)
       
        # TERM 1
             
        self.ids.t1_weeks_no.text = [data[self.year.text]["TERM 1"]["weeks"] for data in calendas if self.year.text in data][0]
        self.ids.t1_opening_date.text = [data[self.year.text]["TERM 1"]["term_dates"]["opening"] for data in calendas if self.year.text in data][0]
        self.ids.t1_closing_date.text = [data[self.year.text]["TERM 1"]["term_dates"]["closing"] for data in calendas if self.year.text in data][0]
        
        self.ids.t1_ht_sdate.text = [data[self.year.text]["TERM 1"]["half_term"]["start"] for data in calendas if self.year.text in data][0]
        self.ids.t1_ht_edate.text = [data[self.year.text]["TERM 1"]["half_term"]["end"] for data in calendas if self.year.text in data][0]
        
        self.ids.t1_holiday_sdate.text = [data[self.year.text]["TERM 1"]["holiday"]["start"] for data in calendas if self.year.text in data][0]
        self.ids.t1_holiday_edate.text = [data[self.year.text]["TERM 1"]["holiday"]["end"] for data in calendas if self.year.text in data][0]
        
        # TERM 2
             
        self.ids.t2_weeks_no.text = [data[self.year.text]["TERM 2"]["weeks"] for data in calendas if self.year.text in data][0]
        self.ids.t2_opening_date.text = [data[self.year.text]["TERM 2"]["term_dates"]["opening"] for data in calendas if self.year.text in data][0]
        self.ids.t2_closing_date.text = [data[self.year.text]["TERM 2"]["term_dates"]["closing"] for data in calendas if self.year.text in data][0]
        
        self.ids.t2_ht_sdate.text = [data[self.year.text]["TERM 2"]["half_term"]["start"] for data in calendas if self.year.text in data][0]
        self.ids.t2_ht_edate.text = [data[self.year.text]["TERM 2"]["half_term"]["end"] for data in calendas if self.year.text in data][0]
        
        self.ids.t2_holiday_sdate.text = [data[self.year.text]["TERM 2"]["holiday"]["start"] for data in calendas if self.year.text in data][0]
        self.ids.t2_holiday_edate.text = [data[self.year.text]["TERM 2"]["holiday"]["end"] for data in calendas if self.year.text in data][0]
        
        # TERM 3
             
        self.ids.t3_weeks_no.text = [data[self.year.text]["TERM 3"]["weeks"] for data in calendas if self.year.text in data][0]
        self.ids.t3_opening_date.text = [data[self.year.text]["TERM 3"]["term_dates"]["opening"] for data in calendas if self.year.text in data][0]
        self.ids.t3_closing_date.text = [data[self.year.text]["TERM 3"]["term_dates"]["closing"] for data in calendas if self.year.text in data][0]
        
        self.ids.t3_ht_sdate.text = [data[self.year.text]["TERM 3"]["half_term"]["start"] for data in calendas if self.year.text in data][0]
        self.ids.t3_ht_edate.text = [data[self.year.text]["TERM 3"]["half_term"]["end"] for data in calendas if self.year.text in data][0]
        
        self.ids.kpsea_sdate.text = [data[self.year.text]["TERM 3"]["kpsea"]["start"] for data in calendas if self.year.text in data][0]
        self.ids.kpsea_edate.text = [data[self.year.text]["TERM 3"]["kpsea"]["end"] for data in calendas if self.year.text in data][0]
        
        self.ids.kcse_sdate.text = [data[self.year.text]["TERM 3"]["kcse"]["start"] for data in calendas if self.year.text in data][0]
        self.ids.kcse_edate.text = [data[self.year.text]["TERM 3"]["kcse"]["end"] for data in calendas if self.year.text in data][0]
        
        self.ids.t3_holiday_sdate.text = [data[self.year.text]["TERM 3"]["holiday"]["start"] for data in calendas if self.year.text in data][0]
        self.ids.t3_holiday_edate.text = [data[self.year.text]["TERM 3"]["holiday"]["end"] for data in calendas if self.year.text in data][0]
        
        
    def update_schcalendar(self):
        t1_tds = {"opening": self.ids.t1_opening_date.text,
                  "closing": self.ids.t1_closing_date.text
        }
        
        t1_hts = {"start": self.ids.t1_ht_sdate.text,
                  "end": self.ids.t1_ht_edate.text
        }
        
        t1_hds = {"start": self.ids.t1_holiday_sdate.text,
                  "end": self.ids.t1_holiday_edate.text
        }
        
        t2_tds = {"opening": self.ids.t2_opening_date.text,
                  "closing": self.ids.t2_closing_date.text
        }
        
        t2_hts = {"start": self.ids.t2_ht_sdate.text,
                  "end": self.ids.t2_ht_edate.text
        }
        
        t2_hds = {"start": self.ids.t2_holiday_sdate.text,
                  "end": self.ids.t2_holiday_edate.text
        }
        
        t3_tds = {"opening": self.ids.t3_opening_date.text,
                  "closing": self.ids.t3_closing_date.text
        }
        
        t3_hts = {"start": self.ids.t3_ht_sdate.text,
                  "end": self.ids.t3_ht_edate.text
        }
        
        t3_hds = {"start": self.ids.t3_holiday_sdate.text,
                  "end": self.ids.t3_holiday_edate.text
        }
        
        kpsea = {"start": self.ids.kpsea_sdate.text,
                  "end": self.ids.kpsea_edate.text
        }
        
        kcse = {"start": self.ids.kcse_sdate.text,
                "end": self.ids.kcse_edate.text
        }
         
        calobj = SchoolCalendar()
        calobj.update_schcalendar(self.ids.t1_weeks_no.text, 
                                  t1_tds, 
                                  t1_hts, 
                                  t1_hds, 
                                  self.ids.t2_weeks_no.text, 
                                  t2_tds, 
                                  t2_hts, 
                                  t2_hds, 
                                  self.ids.t3_weeks_no.text, 
                                  t3_tds, 
                                  t3_hts, 
                                  t3_hds, 
                                  kpsea, 
                                  kcse)
        
        show_toast("Updated school calendar.")
        
        return
        
    # TERM 1
    
    def open_t1_opening_date_picker(self):
        date = MDDatePicker(year=2024)
        date.bind(on_save=self.on_t1_opening_date_changed)
        date.open()
        
    def on_t1_opening_date_changed(self, instance, value, date_range):
        self.ids.t1_opening_date.text = str(value)
        
    #
    
    def open_t1_closing_date_picker(self):
        date = MDDatePicker(year=2024)
        date.bind(on_save=self.on_t1_closing_date_changed)
        date.open()
        
    def on_t1_closing_date_changed(self, instance, value, date_range):
        self.ids.t1_closing_date.text = str(value)
        
    ##
    
    def open_t1_ht_sdate_picker(self):
        date = MDDatePicker(year=2024)
        date.bind(on_save=self.on_t1_ht_sdate_changed)
        date.open()
        
    def on_t1_ht_sdate_changed(self, instance, value, date_range):
        self.ids.t1_ht_sdate.text = str(value)
        
    #
    
    def open_t1_ht_edate_picker(self):
        date = MDDatePicker(year=2024)
        date.bind(on_save=self.on_t1_ht_edate_changed)
        date.open()
        
    def on_t1_ht_edate_changed(self, instance, value, date_range):
        self.ids.t1_ht_edate.text = str(value)
        
    ##
    
    def open_t1_holiday_sdate_picker(self):
        date = MDDatePicker(year=2024)
        date.bind(on_save=self.on_t1_holiday_sdate_changed)
        date.open()
        
    def on_t1_holiday_sdate_changed(self, instance, value, date_range):
        self.ids.t1_holiday_sdate.text = str(value)
        
    #
    
    def open_t1_holiday_edate_picker(self):
        date = MDDatePicker(year=2024)
        date.bind(on_save=self.on_t1_holiday_edate_changed)
        date.open()
        
    def on_t1_holiday_edate_changed(self, instance, value, date_range):
        self.ids.t1_holiday_edate.text = str(value)
        
    # TERM 2
    
    def open_t2_opening_date_picker(self):
        date = MDDatePicker(year=2024)
        date.bind(on_save=self.on_t2_opening_date_changed)
        date.open()
        
    def on_t2_opening_date_changed(self, instance, value, date_range):
        self.ids.t2_opening_date.text = str(value)
        
    #
    
    def open_t2_closing_date_picker(self):
        date = MDDatePicker(year=2024)
        date.bind(on_save=self.on_t2_closing_date_changed)
        date.open()
        
    def on_t2_closing_date_changed(self, instance, value, date_range):
        self.ids.t2_closing_date.text = str(value)
        
    ##
    
    def open_t2_ht_sdate_picker(self):
        date = MDDatePicker(year=2024)
        date.bind(on_save=self.on_t2_ht_sdate_changed)
        date.open()
        
    def on_t2_ht_sdate_changed(self, instance, value, date_range):
        self.ids.t2_ht_sdate.text = str(value)
        
    #
    
    def open_t2_ht_edate_picker(self):
        date = MDDatePicker(year=2024)
        date.bind(on_save=self.on_t2_ht_edate_changed)
        date.open()
        
    def on_t2_ht_edate_changed(self, instance, value, date_range):
        self.ids.t2_ht_edate.text = str(value)
        
    ##
    
    def open_t2_holiday_sdate_picker(self):
        date = MDDatePicker(year=2024)
        date.bind(on_save=self.on_t2_holiday_sdate_changed)
        date.open()
        
    def on_t2_holiday_sdate_changed(self, instance, value, date_range):
        self.ids.t2_holiday_sdate.text = str(value)
        
    #
    
    def open_t2_holiday_edate_picker(self):
        date = MDDatePicker(year=2024)
        date.bind(on_save=self.on_t2_holiday_edate_changed)
        date.open()
        
    def on_t2_holiday_edate_changed(self, instance, value, date_range):
        self.ids.t2_holiday_edate.text = str(value)
    
    # TERM 3
    
    def open_t3_opening_date_picker(self):
        date = MDDatePicker(year=2024)
        date.bind(on_save=self.on_t3_opening_date_changed)
        date.open()
        
    def on_t3_opening_date_changed(self, instance, value, date_range):
        self.ids.t3_opening_date.text = str(value)
        
    #
    
    def open_t3_closing_date_picker(self):
        date = MDDatePicker(year=2024)
        date.bind(on_save=self.on_t3_closing_date_changed)
        date.open()
        
    def on_t3_closing_date_changed(self, instance, value, date_range):
        self.ids.t3_closing_date.text = str(value)
        
    ##
    
    def open_t3_ht_sdate_picker(self):
        date = MDDatePicker(year=2024)
        date.bind(on_save=self.on_t3_ht_sdate_changed)
        date.open()
        
    def on_t3_ht_sdate_changed(self, instance, value, date_range):
        self.ids.t3_ht_sdate.text = str(value)
        
    #
    
    def open_t3_ht_edate_picker(self):
        date = MDDatePicker(year=2024)
        date.bind(on_save=self.on_t3_ht_edate_changed)
        date.open()
        
    def on_t3_ht_edate_changed(self, instance, value, date_range):
        self.ids.t3_ht_edate.text = str(value)
        
    ##
    
    def open_t3_holiday_sdate_picker(self):
        date = MDDatePicker(year=2024)
        date.bind(on_save=self.on_t3_holiday_sdate_changed)
        date.open()
        
    def on_t3_holiday_sdate_changed(self, instance, value, date_range):
        self.ids.t3_holiday_sdate.text = str(value)
        
    #
    
    def open_t3_holiday_edate_picker(self):
        date = MDDatePicker(year=2024)
        date.bind(on_save=self.on_t3_holiday_edate_changed)
        date.open()
        
    def on_t3_holiday_edate_changed(self, instance, value, date_range):
        self.ids.t3_holiday_edate.text = str(value)
    
    ##
    
    def open_kcse_sdate_picker(self):
        date = MDDatePicker(year=2024)
        date.bind(on_save=self.on_kcse_sdate_changed)
        date.open()
        
    def on_kcse_sdate_changed(self, instance, value, date_range):
        self.ids.kcse_sdate.text = str(value)
        
    #
    
    def open_kcse_edate_picker(self):
        date = MDDatePicker(year=2024)
        date.bind(on_save=self.on_kcse_edate_changed)
        date.open()
        
    def on_kcse_edate_changed(self, instance, value, date_range):
        self.ids.kcse_edate.text = str(value)
        
    ##
    
    def open_kpsea_sdate_picker(self):
        date = MDDatePicker(year=2024)
        date.bind(on_save=self.on_kpsea_sdate_changed)
        date.open()
        
    def on_kpsea_sdate_changed(self, instance, value, date_range):
        self.ids.kpsea_sdate.text = str(value)
        
    #
    
    def open_kpsea_edate_picker(self):
        date = MDDatePicker(year=2024)
        date.bind(on_save=self.on_kpsea_edate_changed)
        date.open()
        
    def on_kpsea_edate_changed(self, instance, value, date_range):
        self.ids.kpsea_edate.text = str(value)