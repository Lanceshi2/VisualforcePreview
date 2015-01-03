import sublime
import sublime_plugin
import webbrowser

class VisualforcePreviewCommand(sublime_plugin.TextCommand):
    def run(self, edit, inputFile=None):
        if self.view.is_dirty():
            sublime.error_message("Please save your file first before preview")
            return
        settings = sublime.load_settings('VisualforcePreview.sublime-settings')
        domain = settings.get("Domain")

        fullFileName = self.view.file_name()
        fileNameList = fullFileName.split('\\');
        VFFileName = fileNameList[-1]
        fileNameWithoutExt = (VFFileName.split('.'))[0]

        url = "https://" + domain + ".salesforce.com/apex/" + fileNameWithoutExt
        webbrowser.open(url) 
