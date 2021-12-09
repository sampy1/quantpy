"""
Command Line Interface CLI

This module controls look and feel as well as communications for
command line interaces. This should be a rather generic module
"""
import datetime as dt
import time
import common_routines as cr

class generic_cli(object):
    
    def __init__(self):
        self.currency_symbol = '$'
        self.percentage_symbol = '%'
        self.colors = {
                'red': [1,31,40],
                'green': [1,32,40],
                'yellow': [1,33,40],
                'rybar':[1,33,41],
                'bybar':[1,33,44],
                'jlab':[7,30,00]
            }

    #print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
    def print_format_table(self):
        """
        prints table of formatted text format options
        """
        for style in range(8):
            for fg in range(30,38):
                s1 = ''
                for bg in range(40,48):
                    format = ';'.join([str(style), str(fg), str(bg)])
                    s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
                print(s1)
            print('\n')
        #print(repr('\x1b[0m'))

    def format_terminal_output(self, txt, style, fg, bg):
        """
            These are hex values that are spcified by a general terminal
            interface. More can be read about this topic <here>
            style =  bold, strike through ect...
            fg = foreground color
            bg = background color
        """
        format = ';'.join([str(style), str(fg), str(bg)])
        s = '\x1b[{}m{}\x1b[0m'.format(format, txt)
        return(s)
    
    def color(self, text, color):
        style = self.colors[color][0]
        fg = self.colors[color][1]
        bg = self.colors[color][2]
        return(self.format_terminal_output(text, style, fg, bg))
               
    def color_currency(self, text, color):
        return(self.color(self.currency(text), color))
                   
    def currency(self, text):
        return('{}{:,.2f}'.format(self.currency_symbol, text))
    
    def percent_format(self, text):
        return('{:,.0f}{}'.format( text, self.percentage_symbol))
    
    def format_time(self):
        """ """
        return time.asctime( time.localtime(time.time()))
    
    def make_menu(self, menu_header="Default Menu Header", menu_list=['item 1','item 2','item 3'], 
                  menu_color="yellow"):
        
        menu_list.insert(0, self.color(menu_header, menu_color))
        menu_list.append("Exit")

        menu = [list(i) for i in list(enumerate(menu_list))] 
        menu[1][1] = "  {} {}: {}".format(u'\u250c', menu[1][1],str(menu[1][0]))        
        for item in menu[2:-1]:
            item[1] = "  {} {}: {}".format(u'\u251c', item[1],str(item[0]))
        #Insert Exit Bracket
        menu[-1][1] = "  {} {}: {}".format(u'\u2514', menu[-1][1],str(menu[-1][0]))
        
        processed_menu = ''
        for item in menu:
            processed_menu += item[1] + '\n'
        
        return(processed_menu)
  
    def make_tree(self, menu_header="Default Menu Header", menu_list=['item 1','item 2','item 3'], 
                  menu_color="yellow"):
        
        if len(menu_list)>1:
            menu_list.insert(0, self.color(menu_header, menu_color))

            menu = [list(i) for i in list(enumerate(menu_list))] 
            menu[1][1] = "  {} {}".format(u'\u250c', menu[1][1])        
            for item in menu[2:-1]:
                item[1] = "  {} {}".format(u'\u251c', item[1])
            menu[-1][1] = "  {} {}".format(u'\u2514', menu[-1][1])
            processed_menu = ''
            for item in menu:
                processed_menu += item[1] + '\n'
        else:
            menu_list.insert(0, self.color(menu_header, menu_color))

            menu = [list(i) for i in list(enumerate(menu_list))] 
            menu[1][1] = "  {} {}".format(u'\x2d', menu[1][1])  
            processed_menu = ''
            
            for item in menu:
                processed_menu += item[1] + '\n'
           
        return(processed_menu)  
    

if __name__ == "__main__":
    cr.clear()
    cli = generic_cli()
    #print(cli.format_time())
    cli.print_format_table()
    menu = cli.make_menu("My Menu", menu_list=["Option 1", "Option 2", "fun fun"])
    print(menu)
    
    menu = cli.make_menu(menu_color="green")
    print(menu)
    