# Есть класс, предоставляющий доступ к набору чисел. Источником этого набора чисел является некоторый файл.
# С определенной периодичностью данные в файле меняются (надо реализовать механизм обновления). Приложение должно
# получать доступ к этим данным и выполнять набор операций над ними (сумма, максимум, минимум и т.д.).При каждой попытке
# доступа к этому набору необходимо вносить запись в лог-файл.При реализации используйте паттерн Proxy (для
# логирования) и другие необходимые паттерны.

from abc import ABC, abstractmethod


class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass


class FileDataSource(DataSource):
    def __init__(self, file_name):
        self.file_name = file_name

    def get_data(self):
        with open(self.file_name, "r") as f:
            return [int(line) for line in f]


class DataSourceProxy(DataSource):
    def __init__(self, data_source, log_file_name=None):
        self.data_source = data_source
        self.log_file_name = log_file_name

    def get_data(self):
        with open(self.log_file_name, "a") as log_file:
            log_file.write("Data request\n")
        data = self.data_source.get_data()
        with open(self.log_file_name, "a") as log_file:
            log_file.write("Data received: %s\n" % data)
        return data


class DataProcessor:
    def __init__(self, data_source):
        self.data_source = data_source

    def sum(self):
        data = self.data_source.get_data()
        sum_result = sum(data)
        with open("data.txt", "w") as f:
            f.write("\n".join(str(num) for num in data))
        return sum_result

    def max(self):
        data = self.data_source.get_data()
        max_result = max(data)
        with open("data.txt", "w") as f:
            f.write("\n".join(str(num) for num in data))
        return max_result

    def min(self):
        data = self.data_source.get_data()
        min_result = min(data)
        with open("data.txt", "w") as f:
            f.write("\n".join(str(num) for num in data))
        return min_result


file_data_source = FileDataSource("data.txt")
proxy_data_source = DataSourceProxy(file_data_source, "log.txt")
processor = DataProcessor(proxy_data_source)
print("Summ:", processor.sum())
print("Max:", processor.max())
print("Min:", processor.min())

# С автоматической сменой данных в файле вообще не додумался, как это сделать