"""Module containing all the logic with respect to the GUI."""

from PyQt6 import QtWidgets

from split_mate.database import init_database


class SplitMateWindow(QtWidgets.QMainWindow):
    """Main window for the app."""

    def __init__(self, *args, **kwargs):
        """Constructor of the class.

        Parameters
        ----------
        args, kwargs
            Arguments from the QMainWindow parent class.
        """
        super().__init__(*args, **kwargs)
        self.setWindowTitle("SplitMate - Finance Tracker")
        self.setGeometry(100, 100, 800, 600)
        init_database()

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QtWidgets.QVBoxLayout(central_widget)

        self.tabs = QtWidgets.QTabWidget()
        main_layout.addWidget(self.tabs)

        # Add user(s):
        self.users_tab = self.create_users_tab()
        self.transactions_tab = self.create_transactions_tab()
        self.expense_types_tab = self.create_expense_types_tab()
        self.debts_tab = self.create_debts_tab()
        self.graphs_tab = self.create_graphs_tab()

        self.tabs.addTab(self.users_tab, "Users")
        self.tabs.addTab(self.transactions_tab, "Transactions")
        self.tabs.addTab(self.expense_types_tab, "Expense Types")
        self.tabs.addTab(self.debts_tab, "Debts")
        self.tabs.addTab(self.graphs_tab, "Graphs")

    def create_users_tab(self) -> QtWidgets.QWidget:
        """Creation of the users tab. The users tab allows to add new users and
        view existing users within the tables.
        """
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()

        # Add user form
        label = QtWidgets.QLabel("Add User:")
        layout.addWidget(label)

        self.user_input = QtWidgets.QLineEdit()
        layout.addWidget(self.user_input)

        add_user_button = QtWidgets.QPushButton("Add User")
        add_user_button.clicked.connect(self.add_user)
        layout.addWidget(add_user_button)

        # User table
        self.user_table = QtWidgets.QTableWidget(0, 1)
        self.user_table.setHorizontalHeaderLabels(["Name"])
        layout.addWidget(self.user_table)

        widget.setLayout(layout)
        return widget

    def create_transactions_tab(self):
        """Create the Transactions tab."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()

        # Add transaction form
        label = QtWidgets.QLabel("Add Transaction:")
        layout.addWidget(label)

        self.transaction_user = QtWidgets.QComboBox()
        self.transaction_user.addItem("Select User")
        layout.addWidget(self.transaction_user)

        self.transaction_amount = QtWidgets.QLineEdit()
        layout.addWidget(self.transaction_amount)

        self.transaction_month = QtWidgets.QComboBox()
        self.transaction_month.addItems([str(i) for i in range(1, 13)])
        layout.addWidget(self.transaction_month)

        self.transaction_year = QtWidgets.QLineEdit()
        layout.addWidget(self.transaction_year)

        self.transaction_type = QtWidgets.QComboBox()
        self.transaction_type.addItem("Select Type")
        layout.addWidget(self.transaction_type)

        self.is_income = QtWidgets.QComboBox()
        self.is_income.addItems(["Income", "Expense"])
        layout.addWidget(self.is_income)

        add_transaction_button = QtWidgets.QPushButton("Add Transaction")
        add_transaction_button.clicked.connect(self.add_transaction)
        layout.addWidget(add_transaction_button)

        widget.setLayout(layout)
        return widget

    def create_expense_types_tab(self):
        """Create the Expense Types tab."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()

        # Add expense type form
        label = QtWidgets.QLabel("Add Expense Type:")
        layout.addWidget(label)

        self.expense_type_input = QtWidgets.QLineEdit()
        layout.addWidget(self.expense_type_input)

        add_expense_type_button = QtWidgets.QPushButton("Add Expense Type")
        add_expense_type_button.clicked.connect(self.add_expense_type)
        layout.addWidget(add_expense_type_button)

        widget.setLayout(layout)
        return widget

    def create_debts_tab(self):
        """Create the Debts tab."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()

        label = QtWidgets.QLabel("Debts Between Users:")
        layout.addWidget(label)

        self.debts_table = QtWidgets.QTableWidget(0, 3)
        self.debts_table.setHorizontalHeaderLabels(["Debtor", "Creditor", "Amount"])
        layout.addWidget(self.debts_table)

        widget.setLayout(layout)
        return widget

    def create_graphs_tab(self):
        """Create the Graphs tab."""
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()

        label = QtWidgets.QLabel("Graphs will be displayed here.")
        layout.addWidget(label)

        widget.setLayout(layout)
        return widget

    def add_user(self):
        """Add a new user."""
        name = self.user_input.text().strip()
        if not name:
            QtWidgets.QMessageBox.warning(
                self, "Error", "Please enter a valid user name."
            )
            return

        # TODO: Add logic to insert the user into the database
        row_count = self.user_table.rowCount()
        self.user_table.insertRow(row_count)
        self.user_table.setItem(row_count, 0, QtWidgets.QTableWidgetItem(name))

        self.user_input.clear()

    def add_transaction(self):
        """Add a new transaction."""
        user = self.transaction_user.currentText()
        amount = self.transaction_amount.text().strip()
        month = self.transaction_month.currentText()
        year = self.transaction_year.text().strip()
        expense_type = self.transaction_type.currentText()
        is_income = self.is_income.currentText()

        if not all([user, amount, month, year, expense_type]):
            QtWidgets.QMessageBox.warning(self, "Error", "Please fill in all fields.")
            return

        # TODO: Add logic to insert the transaction into the database
        QtWidgets.QMessageBox.information(
            self, "Success", "Transaction added successfully."
        )

    def add_expense_type(self):
        """Add a new expense type."""
        type_name = self.expense_type_input.text().strip()
        if not type_name:
            QtWidgets.QMessageBox.warning(
                self, "Error", "Please enter a valid expense type."
            )
            return

        # TODO: Add logic to insert the expense type into the database
        QtWidgets.QMessageBox.information(
            self, "Success", f"Expense type '{type_name}' added successfully."
        )
        self.expense_type_input.clear()
