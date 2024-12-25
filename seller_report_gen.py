from fpdf import FPDF

class SellerReportPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Home Pricing Report', ln=1, align='C')

    def section_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, ln=1, align='L')
        self.ln(2)

    def section_body(self, text):
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 10, text)
        self.ln()

    def add_photo(self, photo_path, x=10, y=None, w=50):
        self.image(photo_path, x=x, y=y, w=w)
        self.ln(55)

def generate_seller_report(output_path):
    pdf = SellerReportPDF()
    pdf.add_page()

    # Property Overview
    pdf.section_title("Property Overview")
    pdf.add_photo("property_image.jpg")  # Replace with actual image path
    pdf.section_body("""Address: 110 Vandelinda Avenue, Teaneck, NJ 07666
Specifications: 6 bedrooms, 5 bathrooms, approximately 3,600 sq ft
Lot Size: 8,759 sq ft
Condition: Well-maintained with modern updates
Special Features: Large patio, landscaped backyard, outdoor kitchen
Estimated Market Value: $1,300,000 - $1,550,000 (based on comparables)""")

    # Recent Comparable Sales
    pdf.section_title("Recent Comparable Sales (Last 6 Months)")
    pdf.section_body("""340 Johnson Ave, Teaneck, NJ 07666
Initial Asking Price: $1,850,000
Sale Price: $1,800,000
Days on Market: 45
Distance from Subject Property: 0.8 miles
Bedrooms/Bathrooms: 8 beds, 6 baths
Square Footage: 4,200 sq ft
Lot Size: 10,000 sq ft
Condition: Excellent, newly renovated
Special Features: Pool, tennis court
Sale Date: October 2024
Annual Property Tax: $10,000""")
    
    # Add more properties similarly...

    # Comparable Properties Currently on the Market
    pdf.section_title("Comparable Properties Currently on the Market")
    pdf.section_body("""266 Johnson Ave, Teaneck, NJ 07666
Initial List Date: September 1, 2024
Days on Market: 60
Initial List Price: $1,400,000
Current Price: $1,350,000
Distance from Subject Property: 0.7 miles
Bedrooms/Bathrooms: 7 beds, 6.5 baths
Square Footage: 3,800 sq ft
Lot Size: 10,500 sq ft
Condition: Excellent
Special Features: Pool, outdoor kitchen
Annual Property Tax: $10,000""")

    # Recommended Pricing Strategy
    pdf.section_title("Recommended Pricing Strategy")
    pdf.section_body("""Low Price (to invite a bidding war): $1,250,000
Middle Price (based on comparables): $1,400,000
High Price (anticipating negotiations): $1,550,000""")

    # Market Analysis
    pdf.section_title("Market Analysis")
    pdf.section_body("""The Teaneck market is currently active, with high demand for larger properties featuring 5+ bedrooms and multiple bathrooms.
Homes in your size range have sold between $1,600,000 and $1,800,000, but your price should consider condition, upgrades, and location.""")

    # Additional Recommendations
    pdf.section_title("Additional Recommendations")
    pdf.section_body("""Preparation: Ensure the home is in excellent condition before listing. Small improvements can yield significant returns.
Marketing: Use professional photos, virtual tours, and a detailed property description to showcase your home’s features.
Flexibility: Be open to adjusting the price based on buyer feedback or market shifts.""")

    # Disclaimer
    pdf.section_title("Disclaimer")
    pdf.section_body("This report is based on publicly available data and market trends. It is intended for informational purposes only and does not constitute professional real estate advice. Buyers and sellers should consult with a licensed attorney for specific guidance.")

    # Output the PDF
    pdf.output(output_path)
    print(f"Seller report saved to {output_path}")

# Generate the seller report
generate_seller_report("seller_report.pdf")
