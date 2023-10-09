from codeinterpreterapi import CodeInterpreterSession, settings, File

from config import configs


settings.OPENAI_API_KEY = configs["OPENAI_API_KEY"]


def write_output(response, prompt: str):
    print("-> Response:", response.content)

    for idx, file in enumerate(response.files):
        out_path = f"./out/{idx}_{prompt.replace(' ', '-').lower()}.png"
        file.save(out_path)
        print("-> Chart is generated as:", out_path)
        print("\n\n")


class ChartGenerator:
    @staticmethod
    def from_promt(prompt: str):
        print("> Request:", prompt)

        with CodeInterpreterSession() as session:
            response = session.generate_response(prompt)
            write_output(response, prompt)

    @staticmethod
    def from_dataset(prompt: str, file_path: str):
        print("> Request:", prompt)

        with CodeInterpreterSession() as session:
            files = [File.from_path(file_path)]

            response = session.generate_response(prompt, files)
            write_output(response, prompt)
