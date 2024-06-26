import tkinter as tk
from tkinter import ttk, messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        
        # Initialize data structure to store contacts
        self.contacts = []
        
        # Create UI elements
        self.create_widgets()
        
    def create_widgets(self):
        # Labels and entries for contact information
        lbl_name = tk.Label(self.root, text="Name:")
        lbl_name.grid(row=0, column=0, sticky=tk.W)
        self.entry_name = tk.Entry(self.root)
        self.entry_name.grid(row=0, column=1)
        
        lbl_phone = tk.Label(self.root, text="Phone:")
        lbl_phone.grid(row=1, column=0, sticky=tk.W)
        self.entry_phone = tk.Entry(self.root)
        self.entry_phone.grid(row=1, column=1)
        
        lbl_email = tk.Label(self.root, text="Email:")
        lbl_email.grid(row=2, column=0, sticky=tk.W)
        self.entry_email = tk.Entry(self.root)
        self.entry_email.grid(row=2, column=1)
        
        lbl_address = tk.Label(self.root, text="Address:")
        lbl_address.grid(row=3, column=0, sticky=tk.W)
        self.entry_address = tk.Entry(self.root)
        self.entry_address.grid(row=3, column=1)
        
        # Buttons for actions
        btn_add = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        btn_add.grid(row=4, column=0, columnspan=2, pady=10)
        
        btn_view = tk.Button(self.root, text="View Contacts", command=self.view_contacts)
        btn_view.grid(row=5, column=0, columnspan=2, pady=10)
        
        btn_search = tk.Button(self.root, text="Search Contact", command=self.search_contact)
        btn_search.grid(row=6, column=0, columnspan=2, pady=10)
        
        btn_update = tk.Button(self.root, text="Update Contact", command=self.update_contact)
        btn_update.grid(row=7, column=0, columnspan=2, pady=10)
        
        btn_delete = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        btn_delete.grid(row=8, column=0, columnspan=2, pady=10)
        
        # Treeview to display contacts
        self.tree = ttk.Treeview(self.root, columns=("Name", "Phone", "Email", "Address"), show="headings")
        self.tree.grid(row=0, column=2, rowspan=9, padx=20)
        
        # Set headings for the treeview
        self.tree.heading("Name", text="Name")
        self.tree.heading("Phone", text="Phone")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Address", text="Address")
        
    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()
        
        if name and phone and email and address:
            contact = {'Name': name, 'Phone': phone, 'Email': email, 'Address': address}
            self.contacts.append(contact)
            
            self.update_treeview()
            self.clear_entries()
            messagebox.showinfo("Contact Added", "Contact added successfully.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")
    
    def view_contacts(self):
        self.clear_treeview()
        for contact in self.contacts:
            self.tree.insert("", tk.END, values=(contact['Name'], contact['Phone'], contact['Email'], contact['Address']))
    
    def search_contact(self):
        query = self.entry_name.get().lower()
        self.clear_treeview()
        for contact in self.contacts:
            if query in contact['Name'].lower():
                self.tree.insert("", tk.END, values=(contact['Name'], contact['Phone'], contact['Email'], contact['Address']))
    
    def update_contact(self):
        selected_item = self.tree.selection()
        if selected_item:
            item = selected_item[0]
            name = self.entry_name.get()
            phone = self.entry_phone.get()
            email = self.entry_email.get()
            address = self.entry_address.get()
            
            self.tree.item(item, values=(name, phone, email, address))
            index = self.tree.index(item)
            self.contacts[index] = {'Name': name, 'Phone': phone, 'Email': email, 'Address': address}
            self.clear_entries()
            messagebox.showinfo("Contact Updated", "Contact updated successfully.")
        else:
            messagebox.showerror("Error", "Please select a contact to update.")
    
    def delete_contact(self):
        selected_item = self.tree.selection()
        if selected_item:
            item = selected_item[0]
            self.tree.delete(item)
            index = self.tree.index(item)
            del self.contacts[index]
            messagebox.showinfo("Contact Deleted", "Contact deleted successfully.")
        else:
            messagebox.showerror("Error", "Please select a contact to delete.")
    
    def update_treeview(self):
        self.view_contacts()  # Refresh the treeview display
    
    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)
    
    def clear_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
