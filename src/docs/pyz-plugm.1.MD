% pyz-plugm(1)
% Markix
% April 2022

# NAME
pyz --plugm - Plugin manager for PyZ

# SYNOPSIS
**pyz plugm** install
**pyz plugm** remove

# DESCRIPTION

PlugM is a plugin manager for the PyZ python shell. The plugins are hosted on a GitHub repository (https://github.com/CodyMarkix/PyZ-plugin-repo) and are downloaded from there. They're then saved into a dedicated plugins folder, stored in **~/.local/share/pyz/plugins**.

# OPTIONS

**[no option]**     Prints a help text

**init**    Initialized PlugM, **THIS IS THE FIRST THING YOU WANT TO RUN BEFORE USING PLUGM!!**

**install [plugin]**    Installs the desired plugin

**remove [plugin]**     Removes the desired plugin

**search [plugin]**     Searches for a plugin

**update**     Updates the list of available packages

# COPYRIGHT

Copyright © 2022 Free Software Foundation, Inc. License GPLv2: GNU
GPL version 2 <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.