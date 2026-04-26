from src.data_loader import Dataloader
from src.cleaner import Datacleaner
from src.analyzer import analyzer

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



