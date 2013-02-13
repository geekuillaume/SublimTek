import sublime, sublime_plugin

class EpiActivate(sublime_plugin.TextCommand):

  def run(self, edit):
    # self.view.set_syntax_file("Packages/SublimTek/SublimTek.tmLanguage")
    tmp = self.view.settings().get("auto_indent")
    self.view.settings().set("auto_indent_bak", tmp)
    self.view.settings().set("auto_indent", "false")

    tmp = self.view.settings().get("detect_indentation")
    self.view.settings().set("detect_indentation_bak", tmp)
    self.view.settings().set("detect_indentation", "false")

    tmp = self.view.settings().get("rulers")
    self.view.settings().set("rulers_bak", tmp)
    self.view.settings().set("rulers", [80])

    tmp = self.view.settings().get("tab_size")
    self.view.settings().set("tab_size_bak", tmp)
    self.view.settings().set("tab_size", 8)

    tmp = self.view.settings().get("translate_tabs_to_spaces")
    self.view.settings().set("translate_tabs_to_spaces_bak", tmp)
    self.view.settings().set("translate_tabs_to_spaces", "false")

    tmp = self.view.settings().get("trim_trailing_white_space_on_save")
    self.view.settings().set("trim_trailing_white_space_on_save_bak", tmp)
    self.view.settings().set("trim_trailing_white_space_on_save", "true")

    self.view.settings().set("sublim_tek_mode", "true")

class EpiDeactivate(sublime_plugin.TextCommand):

  def run(self, edit):

    if self.view.settings().get("sublim_tek_mode") == "true" :
        tmp = self.view.settings().get("auto_indent_bak")
        self.view.settings().set("auto_indent", tmp)

        tmp = self.view.settings().get("detect_indentation_bak")
        self.view.settings().set("detect_indentation", tmp)

        tmp = self.view.settings().get("rulers_bak")
        self.view.settings().set("rulers", tmp)

        tmp = self.view.settings().get("tab_size_bak")
        self.view.settings().set("tab_size", tmp)

        tmp = self.view.settings().get("translate_tabs_to_spaces_bak")
        self.view.settings().set("translate_tabs_to_spaces", tmp)

        tmp = self.view.settings().get("trim_trailing_white_space_on_save_bak")
        self.view.settings().set("trim_trailing_white_space_on_save", tmp)
