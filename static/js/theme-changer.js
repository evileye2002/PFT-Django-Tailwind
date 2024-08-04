class ThemeChanger {
  constructor(options) {
    this.lights = options.lights;
    this.darks = options.darks;
    this.themes = [...options.lights, ...options.darks];
    this.defaultTheme = options.default || this.themes[0];
    this.theme = this.defaultTheme;
  }

  getTheme() {
    const localTheme = localStorage.getItem("theme") || this.defaultTheme;
    if (!this.themes.includes(localTheme)) return this.defaultTheme;

    this.theme = localTheme;

    return this.theme;
  }

  getReverse() {
    if (this.lights.includes(this.theme)) {
      const index = this.lights.indexOf(this.theme);
      return this.darks[index] || null;
    }

    if (this.darks.includes(this.theme)) {
      const index = this.darks.indexOf(this.theme);
      return this.lights[index] || null;
    }

    return null;
  }

  setTheme(newTheme) {
    if (!newTheme) {
      console.error("Theme must be a string.");
      return;
    }

    const html = document.querySelector("html");

    this.theme = newTheme;
    html.setAttribute("data-theme", newTheme);
    localStorage.setItem("theme", newTheme);
  }
}

const themeChanger = new ThemeChanger({
  lights: ["emerald"],
  darks: ["dracula"],
  default: "dracula",
});

themeChanger.setTheme(themeChanger.getTheme());
