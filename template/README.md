# FEniCS conf 2024

Template for book of abstracts for FEniCS 2024

![](thumbnail.png)

- Author: Henrik Finsberg (Simula Research Laboratory)
- Author Website: https://scientificcomputing.github.io/fenics_conf2024
- [Submission Guidelines](https://github.com/scientificcomputing/fenics_conf2024)

## Steps to creating your own template!

- [x] 🆕 Create this repository. Nailed it. 🚀
- [ ] 📑 Replace the `template.tex` with your existing LaTeX template/article
- [ ] 👯‍♀️ Copy in any other style, definitions or images necessary for the template
- [ ] 👩‍🔬 Add the files necessary into `files` list in the `template.yml` ([documentation](https://myst-tools.org/docs/mystjs/jtex/template-yml))
- [ ] 🧙‍♀️ Start replacing template values with `[-options.my_value-]` and put in `[# if parts.abstract #]` conditions to toggle sections on and off ([documentation](https://myst-tools.org/docs/mystjs/jtex/template-rules))
- [ ] 👩🏿‍💻 Install [jtex](https://myst-tools.org/docs/mystjs/jtex) (`npm install -g jtex`) and run `jtex check` ([documentation](https://myst-tools.org/docs/mystjs/jtex/command-line))
- [ ] 🪄 Continue to improve the options in your template for `parts` and `options` ([documentation](https://myst-tools.org/docs/mystjs/jtex/document))
- [ ] 💾 When ready, save your `template.yml` and run `jtex check --fix`, this will add various packages that are auto detected and fix document options ([documentation](https://myst-tools.org/docs/mystjs/jtex/command-line))
- [ ] 🧪 Test with real content: `myst build my-document.md --template ../path/to/template` ([documentation](https://myst-tools.org/docs/mystjs/guide/creating-pdf-documents))
- [ ] 📸 Create a `thumbnail.png` with an accurate screenshot of the template
- [ ] 🧭 Update this README, and check all values in the `template.yml`
- [ ] 🚀 Push to GitHub, and contribute to the [community templates repository](https://github.com/myst-templates/templates)


This template is also adopted from the template at https://github.com/myst-templates/curvenote which is licensed under CC-BY-4.0.
