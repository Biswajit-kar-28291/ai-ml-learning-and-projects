import os
import pandas as pd
from .config import REPORTS_FOLDER, DASHBOARD_FOLDER


class ReportGenerator:
    def __init__(self, analyzer):
        self.analyzer = analyzer
        os.makedirs(REPORTS_FOLDER, exist_ok=True)
        os.makedirs(DASHBOARD_FOLDER, exist_ok=True)

    def generate_kpi_summary(self):
        """Generate KPI summary CSV"""
        kpis = self.analyzer.summary_kpis()
        kpi_df = pd.DataFrame(list(kpis.items()), columns=["KPI", "Value"])

        kpi_path = os.path.join(DASHBOARD_FOLDER, "kpi_summary.csv")
        kpi_df.to_csv(kpi_path, index=False)

        print(f"KPI summary saved to: {kpi_path}")
        return kpi_df

    def generate_top_expensive_items_report(self):
        """Generate top expensive items report CSV"""
        top_items = self.analyzer.top_expensive_items()

        top_items_path = os.path.join(REPORTS_FOLDER, "top_expensive_items.csv")
        top_items.to_csv(top_items_path, index=False)

        print(f"Top expensive items report saved to: {top_items_path}")
        return top_items

    def generate_average_mrp_by_item_type_report(self):
        """Generate average MRP by item type CSV"""
        avg_mrp_item_type = self.analyzer.average_mrp_by_item_type().reset_index()
        avg_mrp_item_type.columns = ["item_type", "average_item_mrp"]

        report_path = os.path.join(REPORTS_FOLDER, "average_mrp_by_item_type.csv")
        avg_mrp_item_type.to_csv(report_path, index=False)

        print(f"Average MRP by item type report saved to: {report_path}")
        return avg_mrp_item_type

    def generate_average_mrp_by_outlet_type_report(self):
        """Generate average MRP by outlet type CSV"""
        avg_mrp_outlet_type = self.analyzer.average_mrp_by_outlet_type().reset_index()
        avg_mrp_outlet_type.columns = ["outlet_type", "average_item_mrp"]

        report_path = os.path.join(REPORTS_FOLDER, "average_mrp_by_outlet_type.csv")
        avg_mrp_outlet_type.to_csv(report_path, index=False)

        print(f"Average MRP by outlet type report saved to: {report_path}")
        return avg_mrp_outlet_type

    def generate_business_insights(self):
        """Generate business insights text file"""
        kpis = self.analyzer.summary_kpis()
        top_item_type = self.analyzer.item_type_distribution().idxmax()
        top_outlet_type = self.analyzer.outlet_type_distribution().idxmax()
        top_location_type = self.analyzer.outlet_location_distribution().idxmax()
        expensive_item = self.analyzer.top_expensive_items(1).iloc[0]

        insights = [
            "Retail Product and Outlet Analytics - Business Insights",
            "=====================================================",
            "",
            f"1. Total number of items analyzed: {kpis['Total Items']}",
            f"2. Average item MRP: {kpis['Average Item MRP']}",
            f"3. Maximum item MRP: {kpis['Maximum Item MRP']}",
            f"4. Minimum item MRP: {kpis['Minimum Item MRP']}",
            f"5. Average item weight: {kpis['Average Item Weight']}",
            "",
            f"6. Most common item type: {top_item_type}",
            f"7. Most common outlet type: {top_outlet_type}",
            f"8. Most common outlet location type: {top_location_type}",
            "",
            "9. Most expensive item details:",
            f"   - Item Identifier: {expensive_item['item_identifier']}",
            f"   - Item Type: {expensive_item['item_type']}",
            f"   - Item MRP: {expensive_item['item_mrp']}",
            "",
            "10. Recommendation:",
            "    - Focus on the most frequent item categories for inventory planning.",
            "    - Analyze high-MRP products separately for premium pricing strategy.",
            "    - Compare outlet types and location tiers for product placement decisions."
        ]

        insights_path = os.path.join(REPORTS_FOLDER, "business_insights.txt")
        with open(insights_path, "w", encoding="utf-8") as file:
            file.write("\n".join(insights))

        print(f"Business insights saved to: {insights_path}")
        return insights

    def generate_all_reports(self):
        """Generate all reports"""
        print("Generating reports...")

        self.generate_kpi_summary()
        self.generate_top_expensive_items_report()
        self.generate_average_mrp_by_item_type_report()
        self.generate_average_mrp_by_outlet_type_report()
        self.generate_business_insights()

        print("All reports generated successfully.")