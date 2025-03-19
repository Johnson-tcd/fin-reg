import streamlit as st
import plotly.express as px
import pandas as pd

# Custom CSS for styling
st.markdown("""
    <style>
        :root {
            --purple-dark: #4a1c61;
            --purple-medium: #6a2c91;
            --gold: #d4af37;
            --gold-light: #f1e5ac;
            --background: #f8f8f8;
            --text-dark: #333;
            --text-light: #f8f8f8;
        }
        
        body {
            background-color: var(--background);
            color: var(--text-dark);
        }
        
        .header {
            background: linear-gradient(135deg, var(--purple-dark), var(--purple-medium));
            color: white;
            padding: 1rem;
            box-shadow: 0 3px 10px rgba(0,0,0,0.2);
        }
        
        .logo {
            display: flex;
            align-items: center;
            font-size: 1.8rem;
            color: var(--text-light);
        }
        
        .logo-icon {
            color: var(--gold);
            font-size: 2rem;
        }
        
        .login-btn {
            background-color: var(--gold);
            color: var(--purple-dark);
            border: none;
            padding: 0.7rem 1.5rem;
            border-radius: 5px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .login-btn:hover {
            background-color: var(--gold-light);
            transform: translateY(-2px);
        }
        
        .hero {
            text-align: center;
            margin-bottom: 3rem;
        }
        
        .hero h2 {
            font-size: 2.2rem;
            color: var(--purple-dark);
            margin-bottom: 1rem;
            border-bottom: 3px solid var(--gold);
            padding-bottom: 0.5rem;
        }
        
        .hero p {
            max-width: 800px;
            font-size: 1.1rem;
            line-height: 1.6;
            margin-bottom: 2rem;
        }
        
        .news-card {
            background-color: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 3px 10px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
            margin-bottom: 20px;
        }
        
        .news-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        
        .news-header {
            background-color: var(--purple-medium);
            color: white;
            padding: 10px 15px;
            font-weight: bold;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .region-tag {
            background-color: var(--gold);
            color: var(--purple-dark);
            padding: 3px 8px;
            border-radius: 3px;
            font-size: 0.8rem;
            font-weight: bold;
        }
        
        .news-body {
            padding: 15px;
        }
        
        .news-title {
            font-size: 1.2rem;
            margin-bottom: 10px;
            color: var(--purple-dark);
        }
        
        .news-date {
            color: #777;
            font-size: 0.8rem;
            margin-bottom: 10px;
        }
        
        .news-summary {
            font-size: 0.95rem;
            line-height: 1.5;
            margin-bottom: 15px;
        }
        
        .news-link {
            color: var(--purple-medium);
            text-decoration: none;
            font-weight: bold;
            display: inline-block;
            margin-top: 10px;
        }
        
        .news-link:hover {
            color: var(--gold);
        }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("""
    <div class="header">
        <div class="logo">
            <span class="logo-icon">⚖️</span>
            <h1>Global Financial Regulations Hub</h1>
        </div>
    </div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
    <div class="hero">
        <h2>Your Global Financial Regulation Center</h2>
        <p>Stay updated with the latest financial regulations and policy changes across major economic regions. Our interactive platform provides real-time updates and comprehensive analysis from regulatory experts worldwide.</p>
    </div>
""", unsafe_allow_html=True)

# Globe Visualization using Plotly
st.markdown("### Interactive Financial Globe")
df = pd.DataFrame({
    'lat': [40, 50, 55, 35, 36, 1.3, 25, -25, -10],
    'lon': [-100, 10, -2, 105, 138, 103.8, 45, 135, -55],
    'name': ['North America', 'European Union', 'United Kingdom', 'China', 'Japan', 'Singapore', 'Middle East', 'Australia', 'Brazil'],
    'color': ['#3a7bd5', '#00d2ff', '#0052cc', '#d70000', '#ff6b6b', '#ff9e00', '#ffd700', '#2ecc71', '#27ae60']
})

fig = px.scatter_geo(df, lat='lat', lon='lon', hover_name='name', color='color', size_max=10)
st.plotly_chart(fig)

# News Section
st.markdown("### Latest Regulation Updates")

news_data = [
    {
        "title": "SEC Finalizes New Climate Disclosure Rules",
        "date": "March 15, 2025",
        "region": "USA",
        "summary": "The Securities and Exchange Commission has approved new climate-related disclosure requirements for public companies, establishing standardized reporting on climate risks and greenhouse gas emissions."
    },
    {
        "title": "European Central Bank Updates Digital Euro Framework",
        "date": "March 12, 2025",
        "region": "EU",
        "summary": "The ECB has published its updated regulatory framework for the digital euro, outlining new compliance requirements for financial institutions and payment service providers."
    },
    {
        "title": "FCA Introduces Enhanced Consumer Protection Rules",
        "date": "March 10, 2025",
        "region": "UK",
        "summary": "The UK's Financial Conduct Authority has implemented new consumer duty regulations requiring financial firms to provide more transparent service and demonstrate better outcomes for retail customers."
    },
    {
        "title": "PBOC Announces New Capital Requirements for Digital Banks",
        "date": "March 8, 2025",
        "region": "China",
        "summary": "China's central bank has unveiled stricter capital adequacy requirements for digital banks and fintech platforms, aiming to strengthen financial stability in the growing digital finance sector."
    },
    {
        "title": "MAS Revises Digital Asset Licensing Framework",
        "date": "March 5, 2025",
        "region": "Singapore",
        "summary": "The Monetary Authority of Singapore has updated its licensing regime for digital asset service providers, introducing new requirements for customer protection and risk management."
    },
    {
        "title": "FATF Updates Anti-Money Laundering Guidelines",
        "date": "March 1, 2025",
        "region": "Global",
        "summary": "The Financial Action Task Force has published revised guidelines on anti-money laundering and counter-terrorist financing measures, with new requirements for virtual assets and cross-border transactions."
    }
]

for news in news_data:
    st.markdown(f"""
        <div class="news-card">
            <div class="news-header">
                <span>Regulatory Update</span>
                <span class="region-tag">{news['region']}</span>
            </div>
            <div class="news-body">
                <h4 class="news-title">{news['title']}</h4>
                <p class="news-date">{news['date']}</p>
                <p class="news-summary">{news['summary']}</p>
                <a href="#" class="news-link">Read More →</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Footer Section
st.markdown("""
    <footer>
        <div class="footer-content">
            <div class="footer-section">
                <h4>Regional Hubs</h4>
                <ul>
                    <li><a href="#">North America</a></li>
                    <li><a href="#">European Union</a></li>
                    <li><a href="#">United Kingdom</a></li>
                    <li><a href="#">Asia Pacific</a></li>
                    <li><a href="#">Middle East</a></li>
                    <li><a href="#">Latin America</a></li>
                </ul>
            </div>
            
            <div class="footer-section">
                <h4>Key Regulators</h4>
                <ul>
                    <li><a href="#">SEC (USA)</a></li>
                    <li><a href="#">ECB (EU)</a></li>
                    <li><a href="#">FCA (UK)</a></li>
                    <li><a href="#">PBOC (China)</a></li>
                    <li><a href="#">MAS (Singapore)</a></li>
                    <li><a href="#">FATF (Global)</a></li>
                </ul>
            </div>
            
            <div class="footer-section">
                <h4>Resources</h4>
                <ul>
                    <li><a href="#">Regulation Database</a></li>
                    <li><a href="#">Policy Analyses</a></li>
                    <li><a href="#">Expert Opinions</a></li>
                    <li><a href="#">Compliance Tools</a></li>
                    <li><a href="#">Events & Webinars</a></li>
                </ul>
            </div>
            
            <div class="footer-section">
                <h4>About Us</h4>
                <ul>
                    <li><a href="#">Our Team</a></li>
                    <li><a href="#">Methodology</a></li>
                    <li><a href="#">Contact Us</a></li>
                    <li><a href="#">Careers</a></li>
                    <li><a href="#">Terms of Service</a></li>
                </ul>
            </div>
        </div>
        
        <div class="copyright">
            &copy; 2025 Global Financial Regulations Hub. All rights reserved.
        </div>
    </footer>
""", unsafe_allow_html=True)
