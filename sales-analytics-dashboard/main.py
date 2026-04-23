from src.data_loader import Dataloader
from src.cleaner import Deatacleaner
from src.analyzer import SalesAnalyzer
from src.visualizer import DataVisualizer
from src.report_generator import ReportGenerator


if __name__=="__main__":
    loader=Dataloader()
    df=loader.load_data()
    loader.show_basic_info(df)

    cleaner= Deatacleaner()
    cleaned_df=cleaner.clean_data(df)
    cleaner.save_cleaned_data(cleaned_df)

    print("\nCleaned Data Preview:")
    print(cleaned_df.head())


    analyzer = SalesAnalyzer(cleaned_df)

    print("\nSummary KPIs:")
    print(analyzer.summary_kpis())

    print("\nItem Type Distribution:")
    print(analyzer.item_type_distribution())

    print("\nFat Content Distribution:")
    print(analyzer.fat_content_distribution())

    print("\nOutlet Type Distribution:")
    print(analyzer.outlet_type_distribution())

    print("\nAverage MRP by Item Type:")
    print(analyzer.average_mrp_by_item_type())

    print("\nTop 10 Expensive Items:")
    print(analyzer.top_expensive_items())

    visualizer = DataVisualizer(cleaned_df)
    visualizer.generate_all_charts()

    report_generator = ReportGenerator(analyzer)
    report_generator.generate_all_reports()