import sqlite3
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox


# Function to initialize the database
def init_db():
    con = sqlite3.connect("phonebook.db")
    cursor = con.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CONTACTS_TABLE (
            Name TEXT NOT NULL,
            Mobile_Number TEXT PRIMARY KEY,
            District TEXT,
            Address TEXT,
            Email TEXT,
            Notes TEXT
        )
    """)
    con.commit()
    return con


class PhoneBook:
    def __init__(self, window, con):
        self.con = con
        self.cursor = self.con.cursor()
        self.window = window
        self.clear(self.window)
        self.main_page_gui()
        self.show_contacts()

    def clear(self, window):
        for widget in window.winfo_children():
            widget.destroy()

    def show_contacts(self):
        search = self.search_entry.get()
        try:
            self.tree.delete(*self.tree.get_children())
            if not search:
                self.cursor.execute("SELECT * FROM CONTACTS_TABLE ORDER BY Name ASC")
            else:
                self.cursor.execute(
                    "SELECT * FROM CONTACTS_TABLE WHERE Mobile_Number LIKE ? OR Name LIKE ?",
                    (f"%{search}%", f"%{search}%"),
                )

            fetch = self.cursor.fetchall()
            for data in fetch:
                self.tree.insert("", "end", values=data)
        except tk.TclError:
            pass

    def edit_contact(self):
        if not self.tree.selection():
            tkMessageBox.showwarning("Error", "Please select a contact first!", icon="warning")
        else:
            cur_item = self.tree.focus()
            contents = self.tree.item(cur_item)
            selected_item = contents["values"]

            self.cursor.execute(
                "SELECT * FROM CONTACTS_TABLE WHERE Mobile_Number = ? OR Mobile_Number = ?",
                (selected_item[1], f"0{selected_item[1]}"),
            )
            fetch = self.cursor.fetchone()

            if fetch:
                self.mobile_before_edit = selected_item[1]
                self.edit_contact_gui(fetch)

    def delete_contact(self):
        if not self.tree.selection():
            tkMessageBox.showwarning("Error", "Please select a contact first!", icon="warning")
        else:
            result = tkMessageBox.askquestion("Warning", "Are you sure you want to delete this record?", icon="warning")
            if result == "yes":
                cur_item = self.tree.focus()
                contents = self.tree.item(cur_item)
                selected_item = contents["values"]

                self.cursor.execute(
                    "DELETE FROM CONTACTS_TABLE WHERE Mobile_Number = ? OR Mobile_Number = ?",
                    (selected_item[1], f"0{selected_item[1]}"),
                )
                self.con.commit()
                self.show_contacts()

    def check_int(self, num):
        return num.isdigit()

    def init_call(self):
        self.clear(self.window)
        self.main_page_gui()
        self.show_contacts()

    def edit_contact_in_db(self, mobile):
        self.cursor.execute(
            "DELETE FROM CONTACTS_TABLE WHERE Mobile_Number = ? OR Mobile_Number = ?",
            (self.mobile_before_edit, f"0{self.mobile_before_edit}"),
        )
        self.save_contact_to_db()

    def save_contact_to_db(self):
        name = self.entries["name"].get()
        mobile = self.entries["mobile"].get()
        district = self.entries["district"].get()  # Can now contain letters
        address = self.entries["address"].get()  # Can now contain letters
        email = self.entries["email"].get()
        notes = self.E6.get("1.0", "end-1c")

        if not name or not mobile:
            tkMessageBox.showwarning("Error", "Please fill in all required fields.", icon="warning")
            return

        if not self.check_int(mobile):  # Only checking if mobile is numeric
            tkMessageBox.showwarning("Error", "Mobile must be numeric.", icon="warning")
            return

        self.cursor.execute(
            "SELECT * FROM CONTACTS_TABLE WHERE Mobile_Number = ? OR Mobile_Number = ?",
            (mobile, f"0{mobile}"),
        )
        res = self.cursor.fetchall()

        if not res:
            self.cursor.execute(
                "INSERT INTO CONTACTS_TABLE VALUES (?, ?, ?, ?, ?, ?)",
                (name, mobile, district, address, email, notes),
            )
            self.con.commit()
            self.init_call()
        else:
            tkMessageBox.showwarning("Error", "A contact with this number already exists.", icon="warning")

    def main_page_gui(self):
        width, height = 1000, 500
        self.window.title("PhoneBook")
        self.window.geometry(f"{width}x{height}+{(self.window.winfo_screenwidth() - width) // 2}+{(self.window.winfo_screenheight() - height) // 2}")
        self.window.resizable(0, 0)
        self.window.config(bg="#4eafc4")

        tk.Label(self.window, text="My PhoneBook", font=("Arial", 17), bg="#4ea0c4", fg="#14213d").pack(pady=20, anchor=tk.W)

        tk.Label(self.window, text="Enter name", font=("Arial", 10), bg="#4ea0c4", fg="#14213d").place(x=300, y=10)
        self.search_entry = tk.Entry(self.window, width=50)
        self.search_entry.place(x=300, y=30)

        tk.Button(self.window, text="Search", command=self.show_contacts).place(x=610, y=26)
        tk.Button(self.window, text="Add", command=self.add_new_contact_gui).place(x=800, y=20)
        tk.Button(self.window, text="Edit", command=self.edit_contact).place(x=850, y=20)
        tk.Button(self.window, text="Delete", bg="#FF2525", fg="#FFFFFF", command=self.delete_contact).place(x=900, y=20)

        self.tree = ttk.Treeview(self.window, columns=("1", "2", "3", "4", "5", "6"), show="headings", height=20)
        self.tree.pack(expand=True, fill=tk.BOTH)

        for i, col in enumerate(["Name", "Mobile", "District", "Address", "Email", "Notes"], 1):
            self.tree.heading(str(i), text=col)
            self.tree.column(str(i), width=150, anchor="center")

        self.show_contacts()

    def add_new_contact_gui(self):
        self.clear(self.window)
        self.window.title("Add Contact")

        tk.Label(self.window, text="Add New Contact", font=("Arial", 16)).pack(pady=10)

        labels = ["Name", "Mobile", "District", "Address", "Email"]
        self.entries = {}

        for label in labels:
            tk.Label(self.window, text=f"{label}:").pack()
            entry = tk.Entry(self.window)
            entry.pack()
            self.entries[label.lower()] = entry

        tk.Label(self.window, text="Notes:").pack()
        self.E6 = tk.Text(self.window, height=4, width=40)
        self.E6.pack()

        tk.Button(self.window, text="Save", command=self.save_contact_to_db).pack(pady=20)
        tk.Button(self.window, text="Back", command=self.init_call).pack(pady=10)


if __name__ == "__main__":
    con = init_db()
    root = tk.Tk()
    app = PhoneBook(root, con)
    root.mainloop()