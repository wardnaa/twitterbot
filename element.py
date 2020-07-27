#TODO element for twitter signup

class element(object):
    
    def __init__(self):
        self.creator = "@wardnaa.a"

    def _table_name(self):
        name_xpath = "//*[@id='react-root']/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/label/div/div[2]/div/input"

        return name_xpath
    
    def _change_to_email(self):
        email_true = "//*[@id='react-root']/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[4]/span"

        return email_true
    
    def _table_email(self):
        email_table = "//*[@id='react-root']/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[3]/label/div/div[2]/div/input"

        return email_table
    
    def _tgl_month(self):
        month = '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[5]/div[3]/div/div[1]/div[2]/select'

        return month
    
    def _tgl_day(self):
        day = '//*[@id = "react-root"]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[5]/div[3]/div/div[2]/div[2]/select'
        

        return day
    
    def _tgl_year(self):
        year = '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[5]/div[3]/div/div[3]/div[2]/select'

        return year
    
    def _next_button(self):
        button = '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div/div/span/span'

        return button
    

    def _sign_up_button(self):
        button = '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/div'

        return button
    
    def _table_verif_code(self):
        table_code = '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/label/div/div[2]/div/input'

        return table_code
    
    def _table_password(self):
        table_password = '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[3]/div/label/div/div[2]/div/input'
        

        return table_password
    
    def _skip_button(self):
        button_skip = '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/div[3]/div/div/span/span'

        return button_skip
    
    def _skip_for_now(self):
        skip = '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div'

        return skip
    
    def _search_bar(self):
        search = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div[2]/input'

        return search
    
    def _my_profile(self):
        profile = '//*[@id="typeaheadDropdown-7"]/div[4]/div/li/div[2]/div[2]/div'

        return profile
    
    def _follow_button(self):
        follow = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div[3]/div/div/div/span/span'

        return follow
    
    def _logout_profile(self):
        log = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[2]/div/div/div[2]'
        
        return log
    
    def _logout_account(self):
        log = '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/a[2]/div/div'

        return log
    
    def _logout_finall(self):
        log = '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div'

        return log
    
    def _username_bot(self):
        bot = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/span'

        return bot


    

    



