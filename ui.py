import tkinter as tk
from tkinter import filedialog


BG = "#eef3fa"
NAV = "#0d1422"
TEXT = "#111827"
MUTED = "#65728a"
BLUE = "#2b63f6"
CYAN = "#28c9e8"
BORDER = "#cfd9e8"
SOFT_BLUE = "#eaf1ff"
GREEN = "#1f8f45"
RED = "#e1313d"


class IntentifyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Intentify")
        self.geometry("1180x780")
        self.minsize(980, 680)
        self.configure(bg=BG)

        self.active_tab = tk.StringVar(value="Analyze")
        self.file_label = tk.StringVar(value="sentences.csv, 5 sentences")
        self.record_label = tk.StringVar(value="0 sentences recorded")
        self.single_sentence = tk.StringVar(
            value="Book me a flight from Hanoi to Tokyo next Friday morning"
        )

        self._build_nav()
        self.content = tk.Frame(self, bg=BG)
        self.content.pack(fill="both", expand=True)
        self.show_analyze()

    def _build_nav(self):
        nav = tk.Frame(self, bg=NAV, height=58)
        nav.pack(fill="x")
        nav.pack_propagate(False)

        brand = tk.Frame(nav, bg=NAV)
        brand.pack(side="left", padx=64)
        tk.Label(brand, text="■", fg=CYAN, bg=NAV, font=("Segoe UI", 12)).pack(
            side="left", pady=14
        )
        tk.Label(
            brand,
            text="Intentify",
            fg="white",
            bg=NAV,
            font=("Segoe UI", 17, "bold"),
        ).pack(side="left", padx=(8, 0), pady=14)

        tabs = tk.Frame(nav, bg=NAV)
        tabs.pack(side="right", padx=88, fill="y")
        for name in ("Analyze", "Batch", "History", "Help"):
            item = tk.Frame(tabs, bg=NAV, width=88)
            item.pack(side="left", fill="y")
            label = tk.Label(
                item,
                text=name,
                fg="white" if name == self.active_tab.get() else "#aeb4c0",
                bg=NAV,
                font=("Segoe UI", 13, "bold" if name == self.active_tab.get() else "normal"),
                cursor="hand2",
            )
            label.pack(expand=True)
            underline = tk.Frame(
                item,
                bg=CYAN if name == self.active_tab.get() else NAV,
                height=3,
            )
            underline.pack(fill="x", side="bottom")
            label.bind("<Button-1>", lambda _event, tab=name: self.switch_tab(tab))

    def switch_tab(self, tab):
        self.active_tab.set(tab)
        self._clear(self)
        self._build_nav()
        self.content = tk.Frame(self, bg=BG)
        self.content.pack(fill="both", expand=True)
        if tab == "Analyze":
            self.show_analyze()
        elif tab == "Batch":
            self.show_batch()
        elif tab == "History":
            self.show_simple_page("History", "Saved checks will appear here.")
        else:
            self.show_simple_page("Help", "Upload, paste, or record English sentences to find intents.")

    def _clear(self, widget):
        for child in widget.winfo_children():
            child.destroy()

    def card(self, parent):
        frame = tk.Frame(parent, bg="white", highlightthickness=1, highlightbackground=BORDER)
        return frame

    def section_header(self, parent, step, title):
        tk.Label(
            parent,
            text=step,
            bg="white",
            fg=BLUE,
            font=("Segoe UI", 11, "bold"),
        ).pack(anchor="w")
        tk.Label(
            parent,
            text=title,
            bg="white",
            fg=TEXT,
            font=("Segoe UI", 16, "bold"),
        ).pack(anchor="w", pady=(8, 20))

    def button(self, parent, text, command=None, primary=False, width=16):
        return tk.Button(
            parent,
            text=text,
            command=command,
            width=width,
            height=2,
            bg=BLUE if primary else "white",
            fg="white" if primary else "#1f56d8",
            activebackground="#1f56d8" if primary else "#eef4ff",
            activeforeground="white" if primary else "#1f56d8",
            relief="solid",
            bd=0 if primary else 1,
            highlightthickness=1,
            highlightbackground=BLUE,
            font=("Segoe UI", 12, "bold" if primary else "normal"),
            cursor="hand2",
        )

    def show_analyze(self):
        page = tk.Frame(self.content, bg=BG)
        page.pack(fill="both", expand=True, padx=84, pady=42)

        tk.Label(
            page,
            text="Find the intent of a sentence",
            bg=BG,
            fg=TEXT,
            font=("Segoe UI", 26, "bold"),
        ).pack(anchor="w")
        tk.Label(
            page,
            text="Enter an English sentence by typing, uploading or speaking. The result shows what the\nperson wants and the key details in it.",
            bg=BG,
            fg=MUTED,
            font=("Segoe UI", 15),
            justify="left",
        ).pack(anchor="w", pady=(12, 26))

        columns = tk.Frame(page, bg=BG)
        columns.pack(fill="both", expand=True)
        left = self.card(columns)
        left.pack(side="left", fill="both", expand=True, padx=(0, 24))
        right = self.card(columns)
        right.pack(side="left", fill="both", expand=True)

        self._build_analyze_input(left)
        self._build_analyze_result(right)

    def _build_analyze_input(self, parent):
        body = tk.Frame(parent, bg="white")
        body.pack(fill="both", expand=True, padx=24, pady=24)
        self.section_header(body, "Step 1", "Add your sentence")

        tk.Label(
            body,
            text="Type or paste text",
            bg="white",
            fg=TEXT,
            font=("Segoe UI", 13, "bold"),
        ).pack(anchor="w")
        text = tk.Text(
            body,
            height=6,
            wrap="word",
            relief="solid",
            bd=1,
            highlightthickness=1,
            highlightbackground="#9ba9c2",
            fg=TEXT,
            font=("Segoe UI", 13),
        )
        text.pack(fill="x", pady=(10, 18))
        text.insert("1.0", self.single_sentence.get())

        examples = tk.Frame(body, bg="white")
        examples.pack(anchor="w", pady=(0, 24))
        tk.Label(examples, text="Examples:", bg="white", fg=MUTED, font=("Segoe UI", 12)).pack(
            side="left"
        )
        for sample in ("Cancel my order", "Weather in Da Nang"):
            link = tk.Label(
                examples,
                text=sample,
                bg="white",
                fg="#1f56d8",
                font=("Segoe UI", 12, "underline"),
                cursor="hand2",
            )
            link.pack(side="left", padx=(18, 0))
            link.bind("<Button-1>", lambda _event, value=sample: self._replace_text(text, value))

        tk.Frame(body, bg=BORDER, height=1).pack(fill="x", pady=(0, 20))

        actions = tk.Frame(body, bg="white")
        actions.pack(anchor="w")
        tk.Label(actions, text="Or use", bg="white", fg=TEXT, font=("Segoe UI", 13, "bold")).pack(
            side="left", padx=(0, 16)
        )
        self.button(actions, "Upload .txt file", self.choose_file, width=15).pack(side="left")
        self.button(actions, "Record voice", self.fake_record, width=15).pack(
            side="left", padx=(18, 0)
        )
        self.button(body, "Find the intent", primary=True, width=18).pack(anchor="w", pady=(22, 0))
        tk.Label(body, text="Clear", bg="white", fg=MUTED, font=("Segoe UI", 12)).pack(
            anchor="w", padx=(220, 0), pady=(0, 0)
        )

    def _build_analyze_result(self, parent):
        body = tk.Frame(parent, bg="white")
        body.pack(fill="both", expand=True, padx=24, pady=24)
        self.section_header(body, "Step 2", "Result")

        tk.Label(body, text="Sentence", bg="white", fg=MUTED, font=("Segoe UI", 12)).pack(anchor="w")
        tk.Label(
            body,
            text=self.single_sentence.get(),
            bg="white",
            fg=TEXT,
            font=("Segoe UI", 13),
            wraplength=460,
            justify="left",
        ).pack(anchor="w", pady=(6, 20))
        tk.Frame(body, bg=BORDER, height=1).pack(fill="x", pady=(0, 22))

        result = tk.Frame(body, bg=SOFT_BLUE, highlightthickness=1, highlightbackground="#b9cdfc")
        result.pack(fill="x", pady=(0, 24))
        tk.Label(
            result,
            text="This sentence is asking to",
            bg=SOFT_BLUE,
            fg=MUTED,
            font=("Segoe UI", 12),
        ).pack(anchor="w", padx=18, pady=(18, 8))
        tk.Label(
            result,
            text="Book a flight",
            bg=SOFT_BLUE,
            fg=TEXT,
            font=("Segoe UI", 24, "bold"),
        ).pack(anchor="w", padx=18)
        tk.Label(
            result,
            text="book_flight",
            bg=SOFT_BLUE,
            fg=MUTED,
            font=("Consolas", 12),
        ).pack(anchor="w", padx=18, pady=(6, 18))

        sure = tk.Frame(body, bg="white")
        sure.pack(fill="x", pady=(0, 24))
        tk.Label(sure, text="●", bg="white", fg=GREEN, font=("Segoe UI", 13)).pack(side="left")
        tk.Label(sure, text="Very sure", bg="white", fg=TEXT, font=("Segoe UI", 13, "bold")).pack(
            side="left", padx=(8, 20)
        )
        bar = tk.Frame(sure, bg="#d7dfec", height=4)
        bar.pack(side="left", fill="x", expand=True)
        tk.Frame(bar, bg=GREEN, height=4, width=280).pack(side="left")
        tk.Label(sure, text="94%", bg="white", fg=TEXT, font=("Segoe UI", 13)).pack(
            side="left", padx=(14, 0)
        )

        tk.Label(body, text="Key details", bg="white", fg=TEXT, font=("Segoe UI", 13, "bold")).pack(
            anchor="w"
        )
        for key, value in (("From", "Hanoi"), ("To", "Tokyo"), ("Date", "Next Friday"), ("Time", "Morning")):
            self.detail_row(body, key, value)
        tk.Label(
            body,
            text="Other possibilities: Check flight status 4%, Other 2%",
            bg="white",
            fg=MUTED,
            font=("Segoe UI", 12),
        ).pack(anchor="w", pady=(22, 0))

    def detail_row(self, parent, key, value):
        row = tk.Frame(parent, bg="white")
        row.pack(fill="x", pady=(10, 0))
        tk.Frame(row, bg=BORDER, height=1).pack(fill="x", pady=(0, 10))
        tk.Label(row, text=key, bg="white", fg=MUTED, font=("Segoe UI", 13)).pack(side="left")
        tk.Label(row, text=value, bg="white", fg=TEXT, font=("Segoe UI", 13, "bold")).pack(
            side="right"
        )

    def show_batch(self):
        page = tk.Frame(self.content, bg=BG)
        page.pack(fill="both", expand=True, padx=64, pady=34)

        tk.Label(
            page,
            text="Check many sentences at once",
            bg=BG,
            fg=TEXT,
            font=("Segoe UI", 22, "bold"),
        ).pack(anchor="w")
        tk.Label(
            page,
            text="Upload a file or paste a list of English sentences. Each one gets an intent, and unclear\nones are flagged for you to review.",
            bg=BG,
            fg=MUTED,
            font=("Segoe UI", 12),
            justify="left",
        ).pack(anchor="w", pady=(10, 22))

        add_card = self.card(page)
        add_card.pack(fill="x", pady=(0, 20))
        self._build_batch_input(add_card)

        result_card = self.card(page)
        result_card.pack(fill="both", expand=True)
        self._build_batch_results(result_card)

    def _build_batch_input(self, parent):
        body = tk.Frame(parent, bg="white")
        body.pack(fill="x", padx=22, pady=20)
        self.section_header(body, "Step 1", "Add your sentences")

        row = tk.Frame(body, bg="white")
        row.pack(fill="x")

        upload = tk.Frame(row, bg="#f5f8ff", highlightthickness=1, highlightbackground=BLUE)
        upload.pack(side="left", fill="both", expand=True)
        tk.Label(
            upload,
            text="Upload a CSV or .txt file",
            bg="#f5f8ff",
            fg=TEXT,
            font=("Segoe UI", 12, "bold"),
        ).pack(anchor="w", padx=18, pady=(20, 8))
        tk.Label(
            upload,
            text="One sentence per row or line",
            bg="#f5f8ff",
            fg=MUTED,
            font=("Segoe UI", 11),
        ).pack(anchor="w", padx=18)
        self.button(upload, "Choose file", self.choose_file, width=12).pack(anchor="w", padx=18, pady=14)
        tk.Label(
            upload,
            textvariable=self.file_label,
            bg="#f5f8ff",
            fg=TEXT,
            font=("Segoe UI", 10),
        ).pack(anchor="w", padx=18, pady=(0, 18))

        paste = tk.Frame(row, bg="white")
        paste.pack(side="left", fill="both", expand=True, padx=18)
        tk.Label(paste, text="Or paste sentences", bg="white", fg=TEXT, font=("Segoe UI", 12, "bold")).pack(
            anchor="w"
        )
        tk.Text(paste, height=6, relief="solid", bd=1, font=("Segoe UI", 11)).pack(
            fill="both", expand=True, pady=(8, 0)
        )

        voice = tk.Frame(row, bg="white", highlightthickness=1, highlightbackground=BORDER)
        voice.pack(side="left", fill="both", expand=True)
        tk.Label(
            voice,
            text="Or record your voice",
            bg="white",
            fg=TEXT,
            font=("Segoe UI", 12, "bold"),
        ).pack(anchor="w", padx=18, pady=(20, 8))
        tk.Label(
            voice,
            text="Say one sentence at a time and pause between\nthem",
            bg="white",
            fg=MUTED,
            font=("Segoe UI", 10),
            justify="left",
        ).pack(anchor="w", padx=18)
        self.button(voice, "Record voice", self.fake_record, width=13).pack(anchor="w", padx=18, pady=12)
        tk.Label(voice, textvariable=self.record_label, bg="white", fg=MUTED, font=("Segoe UI", 10)).pack(
            anchor="w", padx=18
        )

        actions = tk.Frame(body, bg="white")
        actions.pack(anchor="w", pady=(18, 0))
        self.button(actions, "Find the intents", primary=True, width=18).pack(side="left")
        tk.Label(actions, text="Clear", bg="white", fg=MUTED, font=("Segoe UI", 11)).pack(
            side="left", padx=28
        )

    def _build_batch_results(self, parent):
        body = tk.Frame(parent, bg="white")
        body.pack(fill="both", expand=True, padx=22, pady=20)

        head = tk.Frame(body, bg="white")
        head.pack(fill="x")
        title = tk.Frame(head, bg="white")
        title.pack(side="left")
        self.section_header(title, "Step 2", "Results")
        self.button(head, "Download results", width=16).pack(side="right")

        stats = tk.Frame(body, bg="white", highlightthickness=1, highlightbackground=BORDER)
        stats.pack(fill="x")
        for number, label, color in (("5", "Sentences checked", TEXT), ("4", "Confident results", GREEN), ("1", "Need your review", RED)):
            cell = tk.Frame(stats, bg="white")
            cell.pack(side="left", fill="x", expand=True, padx=18, pady=14)
            tk.Label(cell, text=number, bg="white", fg=color, font=("Segoe UI", 22, "bold")).pack(anchor="w")
            tk.Label(cell, text=label, bg="white", fg=color if color != TEXT else MUTED, font=("Segoe UI", 10)).pack(anchor="w")

        filters = tk.Frame(body, bg="white")
        filters.pack(anchor="w", pady=16)
        for text, selected in (("All (5)", True), ("Needs review (1)", False), ("Book a flight (1)", False), ("Cancel an order (1)", False)):
            self.button(filters, text, primary=selected, width=16).pack(side="left", padx=(0, 8))

        table = tk.Frame(body, bg="white", highlightthickness=1, highlightbackground=BORDER)
        table.pack(fill="both", expand=True)
        self.table_row(table, ("Sentence", "What it asks for", "How sure"), header=True)
        rows = [
            ("Book me a flight from Hanoi to Tokyo", "Book a flight\nbook_flight", "●  Very sure  94%", "white", GREEN),
            ("Cancel my order from yesterday", "Cancel an order\ncancel_order", "●  Very sure  91%", "white", GREEN),
            ("What is the weather in Da Nang", "Check the weather\ncheck_weather", "●  Fairly sure  89%", "white", BLUE),
            ("I need to change my hotel and my seat\nMay contain more than one request", "Something else\nother", "●  Needs review  46%", "#fff0f0", RED),
            ("Thanks, that is all", "Something else\nother", "●  Fairly sure  78%", "white", BLUE),
        ]
        for row in rows:
            self.table_row(table, row[:3], bg=row[3], status_color=row[4])

    def table_row(self, parent, values, header=False, bg="white", status_color=TEXT):
        row = tk.Frame(parent, bg="#eef2f8" if header else bg)
        row.pack(fill="x")
        widths = (44, 28, 22)
        for index, value in enumerate(values):
            color = MUTED if header else (status_color if index == 2 else TEXT)
            font = ("Segoe UI", 10, "bold") if header else ("Segoe UI", 11, "bold" if index == 1 else "normal")
            cell = tk.Label(
                row,
                text=value,
                bg="#eef2f8" if header else bg,
                fg=color,
                font=font,
                justify="left",
                anchor="w",
                width=widths[index],
            )
            cell.pack(side="left", fill="x", expand=True, padx=16, pady=12)

    def show_simple_page(self, title, message):
        page = tk.Frame(self.content, bg=BG)
        page.pack(fill="both", expand=True, padx=84, pady=42)
        card = self.card(page)
        card.pack(fill="x")
        tk.Label(card, text=title, bg="white", fg=TEXT, font=("Segoe UI", 24, "bold")).pack(
            anchor="w", padx=26, pady=(26, 10)
        )
        tk.Label(card, text=message, bg="white", fg=MUTED, font=("Segoe UI", 13)).pack(
            anchor="w", padx=26, pady=(0, 26)
        )

    def choose_file(self):
        path = filedialog.askopenfilename(
            title="Choose sentences file",
            filetypes=(("Text or CSV", "*.txt *.csv"), ("All files", "*.*")),
        )
        if path:
            self.file_label.set(path.split("/")[-1])

    def fake_record(self):
        self.record_label.set("Voice recording UI is ready")

    def _replace_text(self, widget, value):
        widget.delete("1.0", "end")
        widget.insert("1.0", value)


if __name__ == "__main__":
    app = IntentifyApp()
    app.mainloop()
