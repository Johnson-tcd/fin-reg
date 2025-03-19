import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
from matplotlib import colors
import matplotlib.cm as cm
import folium
from streamlit_folium import folium_static
from PIL import Image
import base64

class GlobalFinancialRegulationsHub:
    def __init__(self):
        # Set page config
        st.set_page_config(
            page_title="Global Financial Regulations Hub",
            page_icon="⚖️",
            layout="wide",
            initial_sidebar_state="expanded",
        )
        
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
        
        # Set session state for login status if not exists
        if 'logged_in' not in st.session_state:
            st.session_state['logged_in'] = False
            
        if 'username' not in st.session_state:
            st.session_state['username'] = ""
            
        if 'selected_region' not in st.session_state:
            st.session_state['selected_region'] = None
        
        # Create the app
        self.create_app()
    
    def create_app(self):
        """Create the Streamlit app layout"""
        # Custom CSS
        self.apply_custom_css()
        
        # Create sidebar
        self.create_sidebar()
        
        # Create header
        self.create_header()
        
        # Create main content based on navigation
        if st.session_state.get('page', 'home') == 'home':
            self.create_home_page()
        elif st.session_state['page'] == 'regions':
            self.create_regions_page()
        elif st.session_state['page'] == 'news':
            self.create_news_page()
        elif st.session_state['page'] == 'resources':
            self.create_resources_page()
        elif st.session_state['page'] == 'about':
            self.create_about_page()
        
        # Create footer
        self.create_footer()
    
    def apply_custom_css(self):
        """Apply custom CSS styles"""
        st.markdown("""
        <style>
        .main {
            background-color: #f8f8f8;
        }
        .stApp {
            max-width: 1200px;
            margin: 0 auto;
        }
        .header {
            background-color: #4a1c61;
            padding: 1.5rem;
            color: white;
            border-radius: 0.5rem;
            margin-bottom: 1rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .logo-title {
            display: flex;
            align-items: center;
        }
        .hero-section {
            text-align: center;
            padding: 2rem 0;
        }
        .section-title {
            color: #4a1c61;
            font-size: 1.5rem;
            font-weight: bold;
            margin-bottom: 1rem;
        }
        .news-card {
            background-color: white;
            border: 1px solid #ddd;
            border-radius: 0.5rem;
            padding: 0;
            margin-bottom: 1rem;
            overflow: hidden;
        }
        .news-header {
            background-color: #6a2c91;
            color: white;
            padding: 0.5rem 1rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .news-body {
            padding: 1rem;
        }
        .news-title {
            color: #4a1c61;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }
        .news-date {
            color: #777;
            font-size: 0.9rem;
            margin-bottom: 1rem;
        }
        .region-tag {
            background-color: #d4af37;
            color: #4a1c61;
            padding: 0.2rem 0.5rem;
            border-radius: 0.25rem;
            font-size: 0.8rem;
            font-weight: bold;
        }
        .read-more {
            color: #6a2c91;
            text-decoration: none;
            font-weight: bold;
        }
        .footer {
            background-color: #4a1c61;
            color: white;
            padding: 2rem 1rem 1rem 1rem;
            margin-top: 3rem;
            border-radius: 0.5rem;
        }
        .footer-title {
            color: #d4af37;
            font-weight: bold;
            font-size: 1.1rem;
            margin-bottom: 1rem;
        }
        .footer-links a {
            color: white;
            text-decoration: none;
            display: block;
            margin-bottom: 0.5rem;
        }
        .footer-separator {
            border-top: 1px solid #6a2c91;
            margin: 1.5rem 0;
        }
        .footer-copyright {
            text-align: center;
            font-size: 0.9rem;
            color: #ccc;
        }
        .login-btn {
            background-color: #d4af37;
            color: #4a1c61;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 0.25rem;
            font-weight: bold;
            cursor: pointer;
        }
        .stButton>button {
            background-color: #6a2c91;
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 0.25rem;
            font-weight: bold;
        }
        div[data-testid="stExpander"] div[role="button"] p {
            font-size: 1.1rem;
            font-weight: bold;
            color: #4a1c61;
        }
        </style>
        """, unsafe_allow_html=True)
    
    def create_sidebar(self):
        """Create sidebar with navigation and login"""
        with st.sidebar:
            st.markdown("### Navigation")
            
            # Navigation buttons
            if st.button("🏠 Home", key="nav_home"):
                st.session_state['page'] = 'home'
                st.experimental_rerun()
                
            if st.button("🌎 Regional Hubs", key="nav_regions"):
                st.session_state['page'] = 'regions'
                st.experimental_rerun()
                
            if st.button("📰 Latest Updates", key="nav_news"):
                st.session_state['page'] = 'news'
                st.experimental_rerun()
                
            if st.button("📚 Resources", key="nav_resources"):
                st.session_state['page'] = 'resources'
                st.experimental_rerun()
                
            if st.button("ℹ️ About Us", key="nav_about"):
                st.session_state['page'] = 'about'
                st.experimental_rerun()
            
            st.markdown("---")
            
            # Login form
            if not st.session_state['logged_in']:
                st.markdown("### Account Access")
                username = st.text_input("Username")
                password = st.text_input("Password", type="password")
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Login"):
                        if username and password:
                            # In a real app, authenticate against a database
                            st.session_state['logged_in'] = True
                            st.session_state['username'] = username
                            st.success(f"Welcome back, {username}!")
                            st.experimental_rerun()
                        else:
                            st.error("Please enter both username and password")
                
                with col2:
                    if st.button("Register"):
                        if username and password:
                            # In a real app, register in a database
                            st.success(f"Account created for {username}. You can now log in.")
                        else:
                            st.error("Please enter both username and password")
            else:
                st.markdown(f"### Welcome, {st.session_state['username']}!")
                if st.button("Logout"):
                    st.session_state['logged_in'] = False
                    st.session_state['username'] = ""
                    st.experimental_rerun()
    
    def create_header(self):
        """Create the application header"""
        st.markdown("""
        <div class="header">
            <div class="logo-title">
                <span style="font-size: 2rem; margin-right: 10px;">⚖️</span>
                <h1 style="margin: 0; color: white;">Global Financial Regulations Hub</h1>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    def create_home_page(self):
        """Create the home page content"""
        # Hero section
        st.markdown("""
        <div class="hero-section">
            <h2 class="section-title">Your Global Financial Regulation Center</h2>
            <p>Stay updated with the latest financial regulations and policy changes across major economic regions.<br>
            Our interactive platform provides real-time updates and comprehensive analysis from regulatory experts worldwide.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Interactive map
        st.markdown('<h3 class="section-title">Interactive Financial Globe</h3>', unsafe_allow_html=True)
        
        # Create interactive map with folium
        m = folium.Map(location=[20, 0], zoom_start=2, tiles="CartoDB dark_matter")
        
        # Add markers for each region
        for region in self.regions:
            html = f"""
            <div style="width: 300px;">
                <h4 style="color: #4a1c61;">{region['name']}</h4>
                <p>{region['description']}</p>
                <button onclick="window.parent.postMessage({{type: 'streamlit:setComponentValue', value: '{region['name']}'}}, '*')">
                    View Details
                </button>
            </div>
            """
            iframe = folium.IFrame(html=html, width=320, height=180)
            popup = folium.Popup(iframe, max_width=320)
            
            folium.CircleMarker(
                location=[region["position"]["lat"], region["position"]["lng"]],
                radius=8,
                color=region["color"],
                fill=True,
                fill_color=region["color"],
                fill_opacity=0.7,
                popup=popup
            ).add_to(m)
        
        # Display map
        folium_static(m, width=1150, height=500)
        
        # Handle region selection
        if st.session_state.get('selected_region'):
            selected = next((r for r in self.regions if r["name"] == st.session_state['selected_region']), None)
            if selected:
                with st.expander(f"📍 {selected['name']} Details", expanded=True):
                    st.markdown(f"**{selected['description']}**")
                    st.button("View Complete Regulatory Framework", key="view_framework")
        
        # Latest news section
        st.markdown('<h3 class="section-title">Latest Regulation Updates</h3>', unsafe_allow_html=True)
        
        col1, col2 = st.columns([0.9, 0.1])
        with col2:
            if st.button("View All", key="view_all_updates"):
                st.session_state['page'] = 'news'
                st.experimental_rerun()
        
        # Display top 3 news items
        self.display_news_items(self.news[:3])
    
    def create_regions_page(self):
        """Create the regions detail page"""
        st.markdown('<h2 class="section-title">Regional Financial Hubs</h2>', unsafe_allow_html=True)
        
        # Display regions in tabs
        tabs = st.tabs([region["name"] for region in self.regions])
        
        for i, tab in enumerate(tabs):
            with tab:
                region = self.regions[i]
                st.markdown(f"### {region['name']}")
                st.markdown(f"**{region['description']}**")
                
                # Create columns for info
                col1, col2 = st.columns([0.6, 0.4])
                
                with col1:
                    st.markdown("#### Key Regulatory Bodies")
                    if region["name"] == "North America":
                        st.markdown("""
                        - **Securities and Exchange Commission (SEC)**
                        - **Federal Reserve System**
                        - **Commodity Futures Trading Commission (CFTC)**
                        - **Financial Industry Regulatory Authority (FINRA)**
                        - **Office of the Comptroller of the Currency (OCC)**
                        """)
                    elif region["name"] == "European Union":
                        st.markdown("""
                        - **European Central Bank (ECB)**
                        - **European Banking Authority (EBA)**
                        - **European Securities and Markets Authority (ESMA)**
                        - **European Insurance and Occupational Pensions Authority (EIOPA)**
                        """)
                    else:
                        st.markdown("- Regulatory information loading...")
                    
                    st.markdown("#### Recent Regulatory Developments")
                    # Filter news for this region
                    region_news = [n for n in self.news if n["region"] == region["name"] or 
                                   (region["name"] == "North America" and n["region"] == "USA") or
                                   (region["name"] == "European Union" and n["region"] == "EU")]
                    
                    if region_news:
                        for news in region_news:
                            st.markdown(f"**{news['title']}** - {news['date']}")
                            st.markdown(f"_{news['summary']}_")
                    else:
                        st.markdown("No recent updates available for this region.")
                
                with col2:
                    st.markdown("#### Compliance Calendar")
                    st.markdown("""
                    | Date | Event |
                    | ---- | ----- |
                    | Apr 15, 2025 | Q1 Reporting Deadline |
                    | May 01, 2025 | New AML Rules Effective |
                    | Jun 30, 2025 | ESG Disclosure Deadline |
                    """)
                    
                    st.markdown("#### Subscribe to Updates")
                    email = st.text_input("Email address", key=f"email_{region['name']}")
                    if st.button("Subscribe", key=f"subscribe_{region['name']}"):
                        if email:
                            st.success(f"You've subscribed to {region['name']} regulatory updates!")
                        else:
                            st.error("Please enter a valid email address")
    
    def create_news_page(self):
        """Create the news page with all updates"""
        st.markdown('<h2 class="section-title">Latest Regulatory Updates</h2>', unsafe_allow_html=True)
        
        # Add filter options
        col1, col2, col3 = st.columns(3)
        
        with col1:
            region_filter = st.selectbox("Filter by Region", 
                                        ["All Regions"] + list(set(news["region"] for news in self.news)))
        
        with col2:
            type_filter = st.selectbox("Filter by Type", 
                                      ["All Types"] + list(set(news["type"] for news in self.news)))
        
        with col3:
            sort_option = st.selectbox("Sort by", ["Newest First", "Oldest First"])
        
        # Filter and sort news
        filtered_news = self.news.copy()
        
        if region_filter != "All Regions":
            filtered_news = [n for n in filtered_news if n["region"] == region_filter]
            
        if type_filter != "All Types":
            filtered_news = [n for n in filtered_news if n["type"] == type_filter]
        
        # Sort news
        if sort_option == "Newest First":
            # Note: In a real app, convert dates to datetime for proper sorting
            pass
        else:
            filtered_news.reverse()
        
        # Display filtered news
        if filtered_news:
            self.display_news_items(filtered_news)
        else:
            st.info("No updates match your selected filters.")
    
    def create_resources_page(self):
        """Create resources page with tools and documents"""
        st.markdown('<h2 class="section-title">Regulatory Resources</h2>', unsafe_allow_html=True)
        
        # Create tabs for different resource types
        tabs = st.tabs(["Regulatory Database", "Compliance Tools", "Policy Analyses", "Events & Webinars"])
        
        with tabs[0]:
            st.markdown("### Financial Regulations Database")
            st.markdown("Search our comprehensive database of financial regulations from major jurisdictions worldwide.")
            
            col1, col2 = st.columns([0.7, 0.3])
            with col1:
                search_term = st.text_input("Search regulations", placeholder="e.g. ESG disclosure, crypto assets, AML")
            
            with col2:
                jurisdiction = st.selectbox("Jurisdiction", ["All Jurisdictions", "USA", "EU", "UK", "China", "Singapore", "Australia"])
            
            if st.button("Search Database"):
                if search_term:
                    st.success(f"Searching for '{search_term}' in {jurisdiction if jurisdiction != 'All Jurisdictions' else 'all jurisdictions'}")
                    st.info("This feature would connect to a regulatory database in a production application.")
                else:
                    st.error("Please enter a search term")
        
        with tabs[1]:
            st.markdown("### Compliance Assessment Tools")
            
            tool = st.selectbox("Select Tool", [
                "Regulatory Gap Analysis",
                "Compliance Risk Calculator",
                "Cross-Border Compliance Checker",
                "AML/KYC Requirements Analyzer",
                "Regulatory Change Management Tool"
            ])
            
            st.markdown("#### Tool Description")
            if tool == "Regulatory Gap Analysis":
                st.markdown("""
                This tool helps identify gaps in your organization's compliance with financial regulations.
                Upload your current compliance documentation and select the jurisdictions you operate in to
                receive a detailed analysis of regulatory gaps and recommended actions.
                """)
            else:
                st.markdown("Description for the selected tool would appear here.")
            
            st.file_uploader("Upload Compliance Documentation (Optional)", type=["pdf", "docx", "xlsx"])
            
            if st.button("Launch Tool"):
                st.info("This feature would launch the selected compliance tool in a production application.")
        
        with tabs[2]:
            st.markdown("### Expert Policy Analyses")
            
            analyses = [
                {
                    "title": "Digital Asset Regulation Trends for 2025",
                    "author": "Dr. Sarah Chen, Regulatory Policy Expert",
                    "date": "March 5, 2025",
                    "summary": "Analysis of evolving regulatory approaches to cryptocurrencies, NFTs, and digital assets across major financial jurisdictions."
                },
                {
                    "title": "Climate Finance Disclosure Requirements: Global Comparison",
                    "author": "Prof. James Wilson, University of Financial Studies",
                    "date": "February 22, 2025",
                    "summary": "Comparative study of climate-related financial disclosure requirements in the US, EU, UK, and Asia Pacific jurisdictions."
                },
                {
                    "title": "Open Banking Regulatory Landscape",
                    "author": "Maria Rodriguez, Former Banking Regulator",
                    "date": "February 8, 2025",
                    "summary": "Evaluation of open banking implementation and regulatory frameworks across different markets."
                }
            ]
            
            for analysis in analyses:
                with st.expander(f"{analysis['title']} ({analysis['date']})"):
                    st.markdown(f"**Author:** {analysis['author']}")
                    st.markdown(f"**Summary:** {analysis['summary']}")
                    if st.button("Read Full Analysis", key=f"read_{analysis['title']}"):
                        st.info("This feature would open the full analysis document in a production application.")
        
        with tabs[3]:
            st.markdown("### Upcoming Events & Webinars")
            
            events = [
                {
                    "title": "Global Financial Regulation Summit 2025",
                    "date": "April 10-12, 2025",
                    "location": "London, UK & Virtual",
                    "description": "Annual gathering of financial regulators, compliance officers, and policy experts discussing emerging regulatory challenges."
                },
                {
                    "title": "Webinar: Preparing for EU Digital Operational Resilience Act (DORA)",
                    "date": "March 25, 2025",
                    "location": "Online",
                    "description": "Expert panel discussing implementation strategies for the EU's DORA framework for financial institutions."
                },
                {
                    "title": "Workshop: Climate Risk Reporting Compliance",
                    "date": "April 5, 2025",
                    "location": "Singapore & Virtual",
                    "description": "Hands-on workshop for compliance officers on meeting climate-related financial disclosure requirements."
                }
            ]
            
            for event in events:
                st.markdown(f"""
                <div class="news-card">
                    <div class="news-header">
                        <span>{event['date']}</span>
                        <span class="region-tag">{event['location']}</span>
                    </div>
                    <div class="news-body">
                        <h4 class="news-title">{event['title']}</h4>
                        <p>{event['description']}</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("### Subscribe to Events Calendar")
            col1, col2 = st.columns([0.7, 0.3])
            
            with col1:
                email = st.text_input("Email address", key="events_email")
            
            with col2:
                if st.button("Subscribe to Events"):
                    if email:
                        st.success("You've successfully subscribed to our events calendar!")
                    else:
                        st.error("Please enter a valid email address")
    
    def create_about_page(self):
        """Create about page with organization information"""
        st.markdown('<h2 class="section-title">About Global Financial Regulations Hub</h2>', unsafe_allow_html=True)
        
        st.markdown("""
        The Global Financial Regulations Hub is a comprehensive platform designed to help financial professionals 
        navigate the complex landscape of financial regulations worldwide. Our mission is to provide accurate, 
        timely, and actionable regulatory information to compliance officers, legal professionals, policy makers, 
        and financial executives.
        """)
        
        # Team section
        st.markdown("### Our Team")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            #### Dr. Eleanor Patel
            **Chief Regulatory Officer**
            
            Former senior regulator with 20 years of experience in financial oversight across multiple jurisdictions.
            """)
        
        with col2:
            st.markdown("""
            #### Michael Chang
            **Director of Policy Analysis**
            
            Expert in financial policy with background in central banking and international regulatory cooperation.
            """)
            
        with col3:
            st.markdown("""
            #### Dr. Sofia Mendes
            **Head of Regulatory Technology**
            
            Specialist in regulatory technology and compliance automation systems for financial institutions.
            """)
        
        # Methodology section
        st.markdown("### Our Methodology")
        
        st.markdown("""
        Our regulatory information is sourced from:
        
        - **Primary Sources**: Official regulatory texts, consultations, and guidance from regulatory authorities
        - **Expert Analysis**: In-house and partner experts who analyze and contextualize regulatory developments
        - **Industry Feedback**: Ongoing input from financial institutions and compliance professionals
        - **Academic Research**: Partnerships with leading financial regulation research centers
        
        All information undergoes a rigorous verification process before publication to ensure accuracy and relevance.
        """)
        
        # Contact section
        st.markdown("### Contact Us")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **General Inquiries:**  
            info@financialregulationshub.com
            
            **Subscription Services:**  
            subscriptions@financialregulationshub.com
            
            **Press Inquiries:**  
            press@financialregulationshub.com
            """)
            
        with col2:
            name = st.text_input("Name")
            email = st.text_input("Email")
            message = st.text_area("Message")
            
            if st.button("Send Message"):
                if name and email and message:
                    st.success("Thank you for your message. We'll respond shortly!")
                else:
                    st.error("Please complete all fields")
    
    def display_news_items(self, news_items):
        """Display news items in a card format"""
        for news in news_items:
            st.markdown(f"""
            <div class="news-card">
                <div class="news-header">
                    <span>{news['type']}</span>
                    <span class="region-tag">{news['region']}</span>
                </div>
                <div class="news-body">
                    <h4 class="news-title">{news['title']}</h4>
                    <p class="news-date">{news['date']}</p>
                    <p>{news['summary']}</p>
                    <a href="#" class="read-more" onclick="alert('Reading full article!')">Read More →</a>
                </div>
            </div>
            """, unsafe_allow_html=True)
    def create_footer(self):
        """Create application footer with links and copyright"""
        st.markdown("""
        <div class="footer">
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px;">
                <div>
                    <div class="footer-title">Regional Hubs</div>
                    <div class="footer-links">
        <div class="footer-links">
                        <a href="#">North America</a>
                        <a href="#">European Union</a>
                        <a href="#">United Kingdom</a>
                        <a href="#">Asia Pacific</a>
                        <a href="#">Middle East</a>
                    </div>
                </div>
                <div>
                    <div class="footer-title">Resources</div>
                    <div class="footer-links">
                        <a href="#">Regulatory Database</a>
                        <a href="#">Compliance Tools</a>
                        <a href="#">Policy Analyses</a>
                        <a href="#">Events & Webinars</a>
                    </div>
                </div>
                <div>
                    <div class="footer-title">Company</div>
                    <div class="footer-links">
                        <a href="#">About Us</a>
                        <a href="#">Our Team</a>
                        <a href="#">Careers</a>
                        <a href="#">Contact Us</a>
                    </div>
                </div>
                <div>
                    <div class="footer-title">Legal</div>
                    <div class="footer-links">
                        <a href="#">Terms of Service</a>
                        <a href="#">Privacy Policy</a>
                        <a href="#">Cookie Policy</a>
                        <a href="#">Disclaimer</a>
                    </div>
                </div>
            </div>
            
            <div class="footer-separator"></div>
            
            <div class="footer-copyright">
                © {datetime.now().year} Global Financial Regulations Hub. All rights reserved.
            </div>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    app = GlobalFinancialRegulationsHub()
