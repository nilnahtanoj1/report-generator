from datetime import datetime

def generate_report(company_name, persona, overview, news, financials, competitors, insights):
    filename = f"output/{company_name}_{persona}_report.md"
    with open(filename, "w") as f:
        f.write(f"Strategic Report for {company_name}\n")
        f.write(f"**Target Persona** {persona}\n")
        f.write(f"**Generated:** {datetime.now()}\n\n")
        
        f.write("## Company Overview\n")
        f.write(insights + "\n\n")
        
        f.write("## Recent News\n")
        f.write(news + "\n\n")
        
        f.write("## Financials\n")
        f.write(str(financials) + "\n\n")
        
        f.write("## Competitors\n")
        f.write(", ".join(competitors) + "\n\n")
        
    return filename