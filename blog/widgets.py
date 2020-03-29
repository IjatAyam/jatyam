from django.forms import DateTimeInput, Textarea


class XDSoftDateTimePickerInput(DateTimeInput):
    template_name = 'widgets/xdsoft_datetimepicker.html'


class BootstrapMarkdownInput(Textarea):
    template_name = 'widgets/bootstrap_markdown.html'
