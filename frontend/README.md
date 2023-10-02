## Frontend setup

### Install nvm (optional, but recommended)

If you want to use the oh-my-zsh nvm plugin:
1. `PROFILE=/dev/null bash -c 'curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.4/install.sh | bash'`
1. As suggested by the install script, add the following 2 lines to your `~/.zshrc`:
    ```
    export NVM_DIR="$HOME/.nvm"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
    ```
1. `omz plugin enable nvm && omz reload`

Otherwise use:
1. `curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.4/install.sh | bash`
1. `source ~/.zshrc` or `omz reload`

More info here: https://github.com/nvm-sh/nvm#installing-and-updating

### Install npm

Using nvm:

`nvm install v20.5.0`

Using brew:

`brew install node`

### Install required packages

`make jsinstall`

or

```
cd frontend
npm install
```

## Scripts

### Run

**NOTE: npm commands must be run from the `frontend` directory. `make` commands must be run from the repository root directory**

#### `npm start` or `make jsrun`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### Run tests

#### `npm test` or `make jstest`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### Build

#### `npm run build` or `make jsbuild`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### Misc

#### `npm run eject` (see https://create-react-app.dev/docs/available-scripts/#npm-run-eject)
