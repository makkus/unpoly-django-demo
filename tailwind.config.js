/** @type {import('tailwindcss').Config} */
const plugin = require("tailwindcss/plugin");
const { spawnSync } = require("child_process");

// Calls Django to fetch template files
const getTemplateFiles = () => {
  const command = "python3";
  const args = ["manage.py", "tailwind", "list_templates"];
  // Assumes tailwind.config.js is located in the BASE_DIR of your Django project.
  const options = { cwd: __dirname };

  const result = spawnSync(command, args, options);

  if (result.error) {
    throw result.error;
  }

  if (result.status !== 0) {
    console.log(result.stdout.toString(), result.stderr.toString());
    throw new Error(
      `Django management command exited with code ${result.status}`
    );
  }

  const templateFiles = result.stdout
    .toString()
    .split("\n")
    .map((file) => file.trim())
    .filter(function (e) {
      return e;
    }); // Remove empty strings, including last empty line.
  return templateFiles;
};

const paths = [
      ...getTemplateFiles()
]

module.exports = {
  content: paths,
    safelist: [
    'input',
    'input-bordered',
    'select',
    'select-bordered',
    'w-full'
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require("@tailwindcss/typography"),
    require("@tailwindcss/forms"),
    require("@tailwindcss/aspect-ratio"),
    require("@tailwindcss/container-queries"),
    require("daisyui")
  ],
  daisyui: {
    themes: [
          'cupcake',
          'winter'
    ]
  },
};
