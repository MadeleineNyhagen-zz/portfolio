#!/usr/bin/python3
# adapting my html generator script to be editable via a gui

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import HTMLdb
import webbrowser
import os

class HTMLEditor:

    def __init__(self, master):

        master.title('Edit the sale page! What should it say?')
        master.configure(background = '#99ccff')
        master.geometry("500x500")

        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#99ccff')
        self.style.configure('TButton', background = '#99ccff')
        self.style.configure('TLabel', background = '#99ccff', font = ('Helvetica', 11))
        self.style.configure('Header.TLabel', font = ('Helvetica', 18, 'bold'))

        # making a frame header
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        # making the frame body
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        self.frame_content.columnconfigure(0, weight=1)
        self.frame_content.columnconfigure(1, weight=1)
        self.frame_content.columnconfigure(2, weight=1)
        self.frame_content.columnconfigure(3, weight=1)
        self.frame_content.columnconfigure(4, weight=1)
        self.frame_content.columnconfigure(5, weight=1)
        self.frame_content.columnconfigure(6, weight=1)
        self.frame_content.columnconfigure(7, weight=1)

        self.frame_content.rowconfigure(0, weight = 1)
        self.frame_content.rowconfigure(1, weight = 1)
        self.frame_content.rowconfigure(2, weight = 1)
        

        # adding content to the header
        self.picture = PhotoImage(file = 'maru3.gif')
        ttk.Label(self.frame_header, image = self.picture).grid(row = 0, column = 0, rowspan = 2)
        ttk.Label(self.frame_header, text = 'Sale Page Editor', style = 'Header.TLabel').grid(row = 0, column = 1)
        ttk.Label(self.frame_header, wraplength = 300, text = ("Type out the text you'd like to see in the body of our summer sale announcement page. "
                                            "When you're done, hit submit to create it!")).grid(row = 1, column = 1)


        # adding content to the body

        # adding the name entry box
        # label
        self.name_label = ttk.Label(self.frame_content, width = 18, text = 'Page Title: ')
        self.name_label.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 5, stick = 'ne')
        # text entry
        self.name_entry = Text(self.frame_content, height = 1, width = 30, font = ('Helvetica',10))
        self.name_entry.grid(row = 1, column = 0, rowspan = 1, columnspan= 3, padx = 5, pady = 5, stick = 'nw')
        # adding the listbox to contain names of various page versions
        self.name_list = Listbox(self.frame_content, height = 16, width = 30, font = ('Helvetica',10))
        self.name_list.grid(row = 2, column = 0, columnspan = 3, rowspan = 4, padx = 5, pady = 5, stick = 'nw')
        self.name_list.bind('<<ListboxSelect>>', self.select)
        # adding a scrollbar to the listbox
        

        

        # adding the body text entry box
        # label
        self.body_label = ttk.Label(self.frame_content, width = 20, text = 'Body Text: ')
        self.body_label.grid(row = 0, column = 3, columnspan = 2, stick = 'ne')
        # text entry
        self.body_text = Text(self.frame_content, height = 19, width = 40, font = ('Helvetica',10))
        self.body_text.grid(row = 1, column = 3, rowspan = 5, columnspan = 4, padx = 10, pady = 5, stick = 'nw')
        
        # buttons
##        decided against a select button in favor of just binding the select method directly to the Listbox
##        ttk.Button(self.frame_content, text = 'Select', command = self.select).grid(row = 6, column = 0, padx = 5, pady = 5, stick = 'nw')
        ttk.Button(self.frame_content, text = 'Update', command = self.updateItem).grid(row = 6, column = 0, padx = 5, pady = 5, stick = 'n')
        ttk.Button(self.frame_content, text = 'Delete', command = self.deleteItem).grid(row = 6, column = 1, padx = 5, pady = 5, stick = 'n')
        ttk.Button(self.frame_content, text = 'Save', command = self.saveBodyText).grid(row = 6, column = 3, padx = 5, pady = 5, stick = 'n')
        ttk.Button(self.frame_content, text = 'Publish', command = self.publish).grid(row = 6, column = 4, padx = 5, pady = 5, stick = 'n')
        ttk.Button(self.frame_content, text = 'Cancel', command = self.exitGui).grid(row = 6, column = 5, padx = 5, pady = 5, stick = 'n')


    # to check whether you're using a pre-existing title        
    
    def sameName(self):
        title = self.name_entry.get(1.0, 'end')
        if HTMLdb.findTitle(title):
            return True
        else:
            return False
        
    # to list existing titles in listbox
    def populateListbox(self):
        for item in HTMLdb.displayAll():
            # itemnumber = str(item[0])
            name = item[1]
            self.name_list.insert(END, name)

    # to clear the listbox
    def clearListbox(self):
        self.name_list.delete(0, END)

    # to clear the input boxes
    def clearTextboxes(self):
        self.body_text.delete(1.0, 'end')
        self.name_entry.delete(1.0, 'end')        

    # to add new page to database
    def saveBodyText(self):
        title = self.name_entry.get(1.0, 'end')
        content = self.body_text.get(1.0, 'end')
        # check that title input isn't empty
        if title != '\n':
            # check that body input isn't empty
            if content != '\n':
                # check that title doesn't already exist in database
                if self.sameName() == False:
                    # save the page
                    HTMLdb.newPage(title, content)
                    self.clearListbox()
                    self.clearTextboxes()
                    self.populateListbox()
                else:
                    # tell user they're trying to use a pre-existing title
                    messagebox.showwarning(
                        'Title already in use',
                        '{} already exists. Rename your page \n or delete the previous entry'.format(title.strip().capitalize())
                        )
            # tell user they need to add content
            else:
                messagebox.showwarning(
                            'No content',
                            'Please add body content before saving'
                            )
        # if title input is empty, check if body input is also empty
        elif content == '\n':
            # if so, do nothing
            return
        # tell user to title their page
        else:
            messagebox.showwarning(
                        'No title',
                        'Please title this page.'
                        )

    # to delete the selected list item from the database
    def deleteItem(self):
        titlelist = self.name_list.curselection()
        item = titlelist[0]
        title = self.name_list.get(item)
        HTMLdb.deletePage(title)
        self.clearListbox()
        self.clearTextboxes()
        self.populateListbox()
        
    # to update the content of an existing database entry    
    def updateItem(self):
        titlelist = self.name_list.curselection()
        item = titlelist[0]
        title = self.name_list.get(item)
        content = self.body_text.get(1.0, 'end')
        HTMLdb.updatePage(title, content)

    # to display a page's body when the title is selected in the listbox
    def select(self, evt):
        titlelist = self.name_list.curselection()
        self.body_text.delete(1.0, END)
        for item in titlelist:
            title = str(self.name_list.get(item))
            page = HTMLdb.displayItem(title)
            for item in page:
                i = item[0]
                self.body_text.insert(END, i)

##        #not sure whether it's better to use nested for loops, or just access index 0 like so:
##
##        title = self.name_list.get(titlelist[0])
##        content = HTMLdb.displayItem(title)[0]
##        self.body_text.insert(END, content[0])



    def publish(self):
##        self.saveBodyText()
        content = self.body_text.get(1.0, 'end')
        filename = "summersale.html"
        f = open(filename,"w")

        htmltext = '''<html>
    <body>
    {}
    </body>
</html>
        '''.format(content)
        f.write(htmltext)
        f.close()

        print(htmltext)
        webbrowser.open('file://' + os.path.realpath(filename))

    def exitGui(self):
        root.destroy()


##def main():
##    root = Tk()
##    htmleditor = HTMLEditor(root)
##    root.mainloop()

root = Tk()
htmleditor = HTMLEditor(root)
htmleditor.populateListbox()
root.mainloop()

# if __name__ == "__main__": main()
