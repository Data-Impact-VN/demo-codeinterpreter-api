from config import configs
from libs.gpt_code_interpreter import ChartGenerator


def main():
    ChartGenerator.from_promt("Plot the bitcoin chart of year 2023")
    ChartGenerator.from_promt(
        "Plot a monthly bar chart about bitcoin price in year 2022"
    )
    ChartGenerator.from_dataset(
        "Analyze this dataset and plot a pie chart about popularity of artists based on streams",
        "./in/spotify-2023.csv",
    )
    # ChartGenerator.from_dataset("Analyze this numpy dataset and plot something interesting about it.", "./in/iris.npy")


if __name__ == "__main__":
    print("Using OPENAI_API_KEY:", configs["OPENAI_API_KEY"])
    main()
