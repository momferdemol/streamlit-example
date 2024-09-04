{ pkgs, config, ... }:

{
  # devenv debug mode
  devenv.debug = false;

  # environment variables
  env.GREET = "---->> hello! ready to code?";
  env.VERSIONS = "---->> versions";

  # cross-shell prompt
  starship.enable = true;

  # language support
  languages.python = {
    enable = true;
    version = "3.12";
    poetry.enable = true;
    poetry.activate.enable = true;
    poetry.install.enable = true;
  };

  # hello script
  scripts.hello.exec = "echo $GREET";

  # echo versions
  scripts.versions.exec = "
    echo $VERSIONS
    echo
    git --version
    python --version
    poetry --version
  ";

  # enter devenv shell
  enterShell = ''
    echo
    versions
    echo
    hello
    echo
  '';

  # See full devenv reference at https://devenv.sh/reference/options/
}
