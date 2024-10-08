# Каждый год ваша компания предоставляет различным
# государственным организациям финансовую отчетность.
# В зависимости от организации форматы отчетности разные.
# Используя механизм декораторов, решите вопрос
# отчетности для организаций.


from abc import ABC, abstractmethod


class ReportGenerator(ABC):
    @abstractmethod
    def generate_report(self, data):
        pass


def report_decorator(func):
    def wrapper_report(self, data):
        print("Generating report...")
        report = func(self, data)
        print("Report generated successfully!")
        return report
    return wrapper_report


class OrganizationAReportGenerator:
    @report_decorator
    def generate_report(self, data):
        return f"Organization A Report: {data}"


class OrganizationBReportGenerator:
    @report_decorator
    def generate_report(self, data):
        return f"Organization B Report: {data}"


class OrganizationCReportGenerator:
    @report_decorator
    def generate_report(self, data):
        return f"Organization C Report: {data}"


organization_a_report_generator = OrganizationAReportGenerator()
organization_b_report_generator = OrganizationBReportGenerator()
organization_c_report_generator = OrganizationCReportGenerator()


data = "Financial data for 2022"
print("Generating report for Organization A:")
report_a = organization_a_report_generator.generate_report(data)
print(report_a)

print("\nGenerating report for Organization B:")
report_b = organization_b_report_generator.generate_report(data)
print(report_b)

print("\nGenerating report for Organization C:")
report_c = organization_c_report_generator.generate_report(data)
print(report_c)