from src.data_loader import Dataloader
from src.cleaner import Datacleaner
from src.analyzer import analyzer
from src.visualizer import Datavisualizer

if __name__=="__main__":
    loade=Dataloader()
    data=loade.loade_data()
    loade.show_data(data)


    clean=Datacleaner()
    cleand_data= clean.cleaned_data(data)
    clean.save_value(cleand_data)

    analyze=analyzer()
    print(
    analyze.summary_kpis(cleand_data)
    )

    v=Datavisualizer(cleand_data)
    v.zone_wise_total_households()
    v.ward_wise_household_distribution()
    v.bottom_10_wards()
    v.household_distribution()



