import tkinter as tk
from tkinter import ttk, font, messagebox
import json
import webbrowser
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import colors
from mpl_toolkits.basemap import Basemap

class GlobalFinancialRegulationsHub:
    def __init__(self, root):
        self.root = root
        self.root.title("Global Financial Regulations Hub")
        self.root.geometry("1200x800")
        self.root.configure(background="#f8f8f8")
        
        # Define colors
        self.colors = {
            "purple_dark": "#4a1c61",
            "purple_medium": "#6a2c91",
            "gold": "#d4af37",
            "gold_light": "#f1e5ac",
            "background": "#f8f8f8",
            "text_dark": "#333333",
            "text_light": "#f8f8f8"
        }
        
        # Define region data
        self.regions = [
            {"name": "North America", 
             "color": "#3a7bd5", 
             "position": {"lat": 40, "lng": -100},
             "description": "Home to major financial regulators including the SEC, Federal Reserve, and CFTC. Features some of the world's largest financial markets and institutions."},
            {"name": "European Union", 
             "color": "#00d2ff", 
             "position": {"lat": 50, "lng": 10},
             "description": "Governed by the European Central Bank and European Banking Authority. Known for comprehensive financial regulations including MiFID II and GDPR."},
            {"name": "United Kingdom", 
             "color": "#0052cc", 
             "position": {"lat": 55, "lng": -2},
             "description": "Regulated by the Financial Conduct Authority (FCA) and Bank of England. London remains one of the world's premier financial centers."},
            {"name": "China", 
             "color": "#d70000", 
             "position": {"lat": 35, "lng": 105},
             "description": "Financial system overseen by the People's Bank of China (PBOC) and China Banking and Insurance Regulatory Commission (CBIRC)."},
            {"name": "Japan", 
             "color": "#ff6b6b", 
             "position": {"lat": 36, "lng": 138},
             "description": "Financial markets regulated by the Financial Services Agency (FSA). Home to the Tokyo Stock Exchange, one of Asia's largest markets."},
            {"name": "Singapore", 
             "color": "#ff9e00", 
             "position": {"lat": 1.3, "lng": 103.8},
             "description": "Regulated by the Monetary Authority of Singapore (MAS). A leading international financial center with strong regulatory framework."},
            {"name": "Middle East", 
             "color": "#ffd700", 
             "position": {"lat": 25, "lng": 45},
             "description": "Emerging financial hubs include Dubai International Financial Centre (DIFC) and Abu Dhabi Global Market (ADGM)."},
            {"name": "Australia", 
             "color": "#2ecc71", 
             "position": {"lat": -25, "lng": 135},
             "description": "Financial system regulated by the Australian Securities and Investments Commission (ASIC) and Reserve Bank of Australia."},
            {"name": "Brazil", 
             "color": "#27ae60", 
             "position": {"lat": -10, "lng": -55},
             "description": "Largest financial market in Latin America, regulated by the Central Bank of Brazil and Securities and Exchange Commission (CVM)."}
        ]
        
        # News data
        self.news = [
            {
                "type": "Regulatory Update",
                "region": "USA",
                "title": "SEC Finalizes New Climate Disclosure Rules",
                "date": "March 15, 2025",
                "summary": "The Securities and Exchange Commission has approved new climate-related disclosure requirements for public companies, establishing standardized reporting on climate risks and greenhouse gas emissions."
            },
            {
                "type": "Policy Change",
                "region": "EU",
                "title": "European Central Bank Updates Digital Euro Framework",
                "date": "March 12, 2025",
                "summary": "The ECB has published its updated regulatory framework for the digital euro, outlining new compliance requirements for financial institutions and payment service providers."
            },
            {
                "type": "Regulatory Update",
                "region": "UK",
                "title": "FCA Introduces Enhanced Consumer Protection Rules",
                "date": "March 10, 2025",
                "summary": "The UK's Financial Conduct Authority has implemented new consumer duty regulations requiring financial firms to provide more transparent service and demonstrate better outcomes for retail customers."
            },
            {
                "type": "Regulatory Update",
                "region": "China",
                "title": "PBOC Announces New Capital Requirements for Digital Banks",
                "date": "March 8, 2025",
                "summary": "China's central bank has unveiled stricter capital adequacy requirements for digital banks and fintech platforms, aiming to strengthen financial stability in the growing digital finance sector."
            },
            {
                "type": "Policy Change",
                "region": "Singapore",
                "title": "MAS Revises Digital Asset Licensing Framework",
                "date": "March 5, 2025",
                "summary": "The Monetary Authority of Singapore has updated its licensing regime for digital asset service providers, introducing new requirements for customer protection and risk management."
            },
            {
                "type": "Regulatory Update",
                "region": "Global",
                "title": "FATF Updates Anti-Money Laundering Guidelines",
                "date": "March 1, 2025",
                "summary": "The Financial Action Task Force has published revised guidelines on anti-money laundering and counter-terrorist financing measures, with new requirements for virtual assets and cross-border transactions."
            }
        ]
        
        # Create custom fonts
        self.define_fonts()
        
        # Create main content
        self.create_ui()
    
    def define_fonts(self):
        """Define custom fonts for the application"""
        self.header_font = font.Font(family="Segoe UI", size=16, weight="bold")
        self.title_font = font.Font(family="Segoe UI", size=14, weight="bold")
        self.subtitle_font = font.Font(family="Segoe UI", size=12, weight="bold")
        self.normal_font = font.Font(family="Segoe UI", size=10)
        self.small_font = font.Font(family="Segoe UI", size=9)
    
    def create_ui(self):
        """Create the main user interface"""
        # Create header
        self.create_header()
        
        # Create main content frame
        main_frame = tk.Frame(self.root, bg=self.colors["background"], padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create hero section
        self.create_hero_section(main_frame)
        
        # Create globe visualization
        self.create_globe_visualization(main_frame)
        
        # Create news section
        self.create_news_section(main_frame)
        
        # Create footer
        self.create_footer()
    
    def create_header(self):
        """Create the application header"""
        header_frame = tk.Frame(self.root, bg=self.colors["purple_dark"], padx=15, pady=10)
        header_frame.pack(fill=tk.X)
        
        # Logo and title
        logo_frame = tk.Frame(header_frame, bg=self.colors["purple_dark"])
        logo_frame.pack(side=tk.LEFT)
        
        logo_label = tk.Label(logo_frame, text="⚖️", font=font.Font(size=20), bg=self.colors["purple_dark"], fg=self.colors["gold"])
        logo_label.pack(side=tk.LEFT, padx=(0, 10))
        
        title_label = tk.Label(logo_frame, text="Global Financial Regulations Hub", font=self.header_font, bg=self.colors["purple_dark"], fg=self.colors["text_light"])
        title_label.pack(side=tk.LEFT)
        
        # Login button
        login_button = tk.Button(
            header_frame, 
            text="Login / Register", 
            bg=self.colors["gold"], 
            fg=self.colors["purple_dark"],
            font=self.normal_font,
            padx=15,
            pady=5,
            relief=tk.FLAT,
            command=self.show_login_dialog
        )
        login_button.pack(side=tk.RIGHT)
    
    def create_hero_section(self, parent):
        """Create the hero section with title and description"""
        hero_frame = tk.Frame(parent, bg=self.colors["background"], pady=20)
        hero_frame.pack(fill=tk.X)
        
        # Title
        title_label = tk.Label(
            hero_frame, 
            text="Your Global Financial Regulation Center", 
            font=self.header_font,
            bg=self.colors["background"],
            fg=self.colors["purple_dark"]
        )
        title_label.pack(pady=(0, 10))
        
        # Description
        description_label = tk.Label(
            hero_frame, 
            text="Stay updated with the latest financial regulations and policy changes across major economic regions.\n"
                 "Our interactive platform provides real-time updates and comprehensive analysis from regulatory experts worldwide.",
            font=self.normal_font,
            bg=self.colors["background"],
            fg=self.colors["text_dark"],
            justify=tk.CENTER,
            wraplength=800
        )
        description_label.pack(pady=(0, 20))
    
    def create_globe_visualization(self, parent):
        """Create interactive globe visualization using matplotlib and basemap"""
        globe_frame = tk.Frame(parent, bg=self.colors["background"], pady=10)
        globe_frame.pack(fill=tk.X)
        
        # Title
        globe_title = tk.Label(
            globe_frame,
            text="Interactive Financial Globe",
            font=self.subtitle_font,
            bg=self.colors["background"],
            fg=self.colors["purple_dark"]
        )
        globe_title.pack(pady=(0, 10))
        
        # Create matplotlib figure
        self.fig = plt.Figure(figsize=(10, 6), facecolor='#0a0a2a')
        self.ax = self.fig.add_subplot(111)
        
        # Create map using Basemap
        self.m = Basemap(projection='ortho', lat_0=30, lon_0=0, resolution='l', ax=self.ax)
        self.m.drawcoastlines(color='#334756', linewidth=0.5)
        self.m.drawcountries(color='#334756', linewidth=0.5)
        self.m.fillcontinents(color='#1a1a2e', lake_color='#0a0a2a')
        self.m.drawmapboundary(fill_color='#0a0a2a')
        
        # Add region markers
        for region in self.regions:
            x, y = self.m(region["position"]["lng"], region["position"]["lat"])
            self.m.plot(x, y, 'o', markersize=7, color=region["color"], alpha=0.8)
            
        # Remove axis ticks
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        
        # Add title
        self.ax.set_title('Click on a region to view details', color='white', fontsize=10)
        
        # Create canvas and add to frame
        self.canvas = FigureCanvasTkAgg(self.fig, master=globe_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Add interaction
        self.canvas.mpl_connect('button_press_event', self.on_globe_click)
        
        # Info panel frame
        self.info_panel = tk.Frame(globe_frame, bg=self.colors["purple_dark"], padx=15, pady=15, bd=1, relief=tk.SOLID)
        self.info_panel.pack(side=tk.RIGHT, anchor=tk.NE, padx=20, pady=10)
        self.info_panel.pack_forget()  # Hide initially
        
        # Info panel content
        self.region_title = tk.Label(
            self.info_panel,
            text="Region Name",
            font=self.subtitle_font,
            bg=self.colors["purple_dark"],
            fg=self.colors["gold"]
        )
        self.region_title.pack(anchor=tk.W, pady=(0, 10))
        
        self.region_description = tk.Label(
            self.info_panel,
            text="Region description will appear here.",
            font=self.normal_font,
            bg=self.colors["purple_dark"],
            fg=self.colors["text_light"],
            wraplength=300,
            justify=tk.LEFT
        )
        self.region_description.pack(anchor=tk.W, pady=(0, 10))
        
        self.view_details_button = tk.Button(
            self.info_panel,
            text="View Details",
            bg=self.colors["gold"],
            fg=self.colors["purple_dark"],
            font=self.normal_font,
            padx=10,
            pady=5,
            relief=tk.FLAT,
            command=self.view_region_details
        )
        self.view_details_button.pack(anchor=tk.W)
    
    def create_news_section(self, parent):
        """Create the news section with regulation updates"""
        news_frame = tk.Frame(parent, bg=self.colors["background"], pady=20)
        news_frame.pack(fill=tk.X)
        
        # Header frame
        header_frame = tk.Frame(news_frame, bg=self.colors["background"])
        header_frame.pack(fill=tk.X, pady=(20, 15))
        
        # Title
        news_title = tk.Label(
            header_frame,
            text="Latest Regulation Updates",
            font=self.title_font,
            bg=self.colors["background"],
            fg=self.colors["purple_dark"]
        )
        news_title.pack(side=tk.LEFT)
        
        # View all link
        view_all_button = tk.Button(
            header_frame,
            text="View All Updates",
            bg=self.colors["background"],
            fg=self.colors["purple_medium"],
            font=self.normal_font,
            relief=tk.FLAT,
            command=self.view_all_updates
        )
        view_all_button.pack(side=tk.RIGHT)
        
        # News cards container (using canvas for scrolling)
        canvas_frame = tk.Frame(news_frame, bg=self.colors["background"])
        canvas_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create canvas for scrolling
        self.news_canvas = tk.Canvas(canvas_frame, bg=self.colors["background"], highlightthickness=0)
        self.news_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(canvas_frame, orient=tk.VERTICAL, command=self.news_canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.news_canvas.configure(yscrollcommand=scrollbar.set)
        
        # Create inner frame for news cards
        self.news_inner_frame = tk.Frame(self.news_canvas, bg=self.colors["background"])
        self.news_canvas.create_window((0, 0), window=self.news_inner_frame, anchor=tk.NW)
        
        # Add news cards
        self.create_news_cards()
        
        # Update inner frame size for scrolling
        self.news_inner_frame.update_idletasks()
        self.news_canvas.config(scrollregion=self.news_canvas.bbox("all"))
    
    def create_news_cards(self):
        """Create cards for each news item"""
        # Configure grid layout
        self.news_inner_frame.columnconfigure(0, weight=1)
        self.news_inner_frame.columnconfigure(1, weight=1)
        self.news_inner_frame.columnconfigure(2, weight=1)
        
        # Add news cards in a grid
        row, col = 0, 0
        for i, news_item in enumerate(self.news):
            # Calculate grid position
            if i % 3 == 0 and i > 0:
                row += 1
                col = 0
            
            # Create card frame
            card_frame = tk.Frame(self.news_inner_frame, bg="white", bd=1, relief=tk.SOLID, width=350)
            card_frame.grid(row=row, column=col, padx=10, pady=10, sticky=tk.NSEW)
            
            # Card header
            card_header = tk.Frame(card_frame, bg=self.colors["purple_medium"], padx=10, pady=5)
            card_header.pack(fill=tk.X)
            
            # Header content
            header_left = tk.Label(
                card_header,
                text=news_item["type"],
                font=self.small_font,
                bg=self.colors["purple_medium"],
                fg=self.colors["text_light"]
            )
            header_left.pack(side=tk.LEFT)
            
            # Region tag
            region_tag = tk.Label(
                card_header,
                text=news_item["region"],
                font=self.small_font,
                bg=self.colors["gold"],
                fg=self.colors["purple_dark"],
                padx=5,
                pady=1
            )
            region_tag.pack(side=tk.RIGHT)
            
            # Card body
            card_body = tk.Frame(card_frame, bg="white", padx=15, pady=15)
            card_body.pack(fill=tk.BOTH, expand=True)
            
            # News title
            news_title = tk.Label(
                card_body,
                text=news_item["title"],
                font=self.subtitle_font,
                bg="white",
                fg=self.colors["purple_dark"],
                wraplength=300,
                justify=tk.LEFT
            )
            news_title.pack(anchor=tk.W)
            
            # News date
            news_date = tk.Label(
                card_body,
                text=news_item["date"],
                font=self.small_font,
                bg="white",
                fg="#777777"
            )
            news_date.pack(anchor=tk.W, pady=(5, 10))
            
            # News summary
            news_summary = tk.Label(
                card_body,
                text=news_item["summary"],
                font=self.normal_font,
                bg="white",
                fg=self.colors["text_dark"],
                wraplength=300,
                justify=tk.LEFT
            )
            news_summary.pack(anchor=tk.W, pady=(0, 10))
            
            # Read more link
            read_more = tk.Button(
                card_body,
                text="Read More →",
                bg="white",
                fg=self.colors["purple_medium"],
                font=self.normal_font,
                relief=tk.FLAT,
                command=lambda item=news_item: self.read_more(item)
            )
            read_more.pack(anchor=tk.W)
            
            # Update column counter
            col += 1
    
    def create_footer(self):
        """Create application footer with links and copyright"""
        footer_frame = tk.Frame(self.root, bg=self.colors["purple_dark"], padx=15, pady=20)
        footer_frame.pack(fill=tk.X)
        
        # Create content frame
        content_frame = tk.Frame(footer_frame, bg=self.colors["purple_dark"])
        content_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Create four sections
        sections = [
            {
                "title": "Regional Hubs",
                "links": ["North America", "European Union", "United Kingdom", "Asia Pacific", "Middle East", "Latin America"]
            },
            {
                "title": "Key Regulators",
                "links": ["SEC (USA)", "ECB (EU)", "FCA (UK)", "PBOC (China)", "MAS (Singapore)", "FATF (Global)"]
            },
            {
                "title": "Resources",
                "links": ["Regulation Database", "Policy Analyses", "Expert Opinions", "Compliance Tools", "Events & Webinars"]
            },
            {
                "title": "About Us",
                "links": ["Our Team", "Methodology", "Contact Us", "Careers", "Terms of Service"]
            }
        ]
        
        # Create each section
        for i, section in enumerate(sections):
            section_frame = tk.Frame(content_frame, bg=self.colors["purple_dark"], padx=10)
            section_frame.grid(row=0, column=i, sticky=tk.N)
            
            # Title
            title = tk.Label(
                section_frame,
                text=section["title"],
                font=self.subtitle_font,
                bg=self.colors["purple_dark"],
                fg=self.colors["gold"]
            )
            title.pack(anchor=tk.W, pady=(0, 10))
            
            # Links
            for link in section["links"]:
                link_button = tk.Button(
                    section_frame,
                    text=link,
                    bg=self.colors["purple_dark"],
                    fg=self.colors["text_light"],
                    font=self.normal_font,
                    relief=tk.FLAT,
                    anchor=tk.W,
                    command=lambda l=link: self.open_link(l)
                )
                link_button.pack(anchor=tk.W, pady=2)
        
        # Copyright
        copyright_frame = tk.Frame(footer_frame, bg=self.colors["purple_dark"], padx=10, pady=10)
        copyright_frame.pack(fill=tk.X)
        
        separator = ttk.Separator(copyright_frame, orient=tk.HORIZONTAL)
        separator.pack(fill=tk.X, pady=(0, 10))
        
        copyright_text = tk.Label(
            copyright_frame,
            text="© 2025 Global Financial Regulations Hub. All rights reserved.",
            font=self.small_font,
            bg=self.colors["purple_dark"],
            fg=self.colors["text_light"]
        )
        copyright_text.pack()
    
    # Event handlers and utility methods
    def show_login_dialog(self):
        """Show login/register dialog"""
        login_window = tk.Toplevel(self.root)
        login_window.title("Login / Register")
        login_window.geometry("400x300")
        login_window.configure(bg=self.colors["background"])
        
        # Center window
        login_window.transient(self.root)
        login_window.grab_set()
        
        # Title
        title_label = tk.Label(
            login_window,
            text="Account Access",
            font=self.title_font,
            bg=self.colors["background"],
            fg=self.colors["purple_dark"]
        )
        title_label.pack(pady=(20, 30))
        
        # Login form
        form_frame = tk.Frame(login_window, bg=self.colors["background"])
        form_frame.pack(fill=tk.X, padx=50)
        
        # Username
        username_label = tk.Label(
            form_frame,
            text="Username:",
            font=self.normal_font,
            bg=self.colors["background"],
            fg=self.colors["text_dark"]
        )
        username_label.pack(anchor=tk.W, pady=(0, 5))
        
        username_entry = tk.Entry(form_frame, font=self.normal_font, width=30)
        username_entry.pack(fill=tk.X, pady=(0, 15))
        
        # Password
        password_label = tk.Label(
            form_frame,
            text="Password:",
            font=self.normal_font,
            bg=self.colors["background"],
            fg=self.colors["text_dark"]
        )
        password_label.pack(anchor=tk.W, pady=(0, 5))
        
        password_entry = tk.Entry(form_frame, font=self.normal_font, width=30, show="*")
        password_entry.pack(fill=tk.X, pady=(0, 25))
        
        # Buttons
        buttons_frame = tk.Frame(form_frame, bg=self.colors["background"])
        buttons_frame.pack(fill=tk.X)
        
        login_btn = tk.Button(
            buttons_frame,
            text="Login",
            bg=self.colors["purple_dark"],
            fg=self.colors["text_light"],
            font=self.normal_font,
            padx=15,
            pady=5,
            relief=tk.FLAT,
            command=lambda: self.login(username_entry.get(), password_entry.get(), login_window)
        )
        login_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        register_btn = tk.Button(
            buttons_frame,
            text="Register",
            bg=self.colors["gold"],
            fg=self.colors["purple_dark"],
            font=self.normal_font,
            padx=15,
            pady=5,
            relief=tk.FLAT,
            command=lambda: self.register(username_entry.get(), password_entry.get(), login_window)
        )
        register_btn.pack(side=tk.LEFT)
    
    def login(self, username, password, window):
        """Handle login action"""
        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password.")
            return
        
        # This is a mock login that would connect to a backend in a real app
        messagebox.showinfo("Login Successful", f"Welcome back, {username}!")
        window.destroy()
    
    def register(self, username, password, window):
        """Handle register action"""
        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password.")
            return
        
        # This is a mock registration that would connect to a backend in a real app
        messagebox.showinfo("Registration Successful", f"Account created for {username}. You can now log in.")
        window.destroy()
    
    def on_globe_click(self, event):
        """Handle click on the globe map"""
        # Get x, y coordinates of click
        x, y = event.xdata, event.ydata
        
        if x is None or y is None:
            return
        
        # Convert to lon/lat
        lon, lat = self.m(x, y, inverse=True)
        
        # Find nearest region
        closest_region = None
        min_distance = float('inf')
        
        for region in self.regions:
            r_lon = region["position"]["lng"]
            r_lat = region["position"]["lat"]
            
            # Calculate distance (simple Euclidean)
            dist = ((lon - r_lon) ** 2 + (lat - r_lat) ** 2) ** 0.5
            
            if dist < min_distance and dist < 20:  # Within certain threshold
                min_distance = dist
                closest_region = region
        
        if closest_region:
            # Update info panel
            self.region_title.config(text=closest_region["name"])
            self.region_description.config(text=closest_region["description"])
            
            # Show info panel
            self.info_panel.pack(side=tk.RIGHT, anchor=tk.NE, padx=20, pady=10)
            
            # Store selected region
            self.selected_region = closest_region
    
    def view_region_details(self):
        """Handle click on View Details button for a region"""
        if hasattr(self, 'selected_region'):
            messagebox.showinfo("Region Details", f"Viewing detailed regulations for {self.selected_region['name']}")
    
    def read_more(self, news_item):
        """Handle click on Read More link for a news item"""
        # In a real app, this would navigate to a detailed view
        messagebox.showinfo("News Details", f"Reading full article: {news_item['title']}")
    
    def view_all_updates(self):
        """Handle click on View All Updates link"""
        messagebox.showinfo("All Updates", "Viewing all regulatory updates")
    
    def open_link(self, link_text):
        """Handle click on a link in the footer"""
        messagebox.showinfo("Navigation", f"Navigating to: {link_text}")


if __name__ == "__main__":
    root = tk.Tk()
    app = GlobalFinancialRegulationsHub(root)
    root.mainloop()
