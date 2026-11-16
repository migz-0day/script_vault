rule ScriptVault_Repo_Artifacts
{
    meta:
        author = "migz-0day"
        description = "Identifies documentation, archives, or entrypoints referencing the script_vault repository"
        repository = "https://github.com/migz-0day/script_vault"
        date = "2026-11-16"
        category = "inventory"

    strings:
        $repo_url = "migz-0day/script_vault" ascii wide nocase
        $repo_name = "script_vault" ascii wide
        $desc = "A collection of useful scripts and automation utilities" ascii wide nocase
        $f1 = "create_project.py" ascii wide
        $f2 = "create_project.sh" ascii wide
        $f3 = "git_to.py" ascii wide
        $f4 = "system.sh" ascii wide
        $f5 = "node_update.py" ascii wide

    condition:
        filesize < 5MB and (
            $repo_url or
            ($repo_name and $desc) or
            (3 of ($f*))
        )
}

rule ScriptVault_Project_Scaffolder
{
    meta:
        author = "migz-0day"
        description = "Detects create_project.py or create_project.sh scaffolding utilities"
        repository = "https://github.com/migz-0day/script_vault"
        category = "developerTools"

    strings:
        $shebang_py = "#!/usr/bin/env python" ascii
        $shebang_sh = "#!/bin/bash" ascii
        $shebang_sh2 = "#!/usr/bin/env bash" ascii
        $fn_name = "create_project" ascii nocase
        $kw_mkdir = "mkdir" ascii
        $kw_os = "os.makedirs" ascii
        $kw_cargo = "cargo" ascii
        $kw_mod = "go mod" ascii

    condition:
        filesize < 500KB and
        ($shebang_py or $shebang_sh or $shebang_sh2) and
        $fn_name and
        any of ($kw_*)
}

rule ScriptVault_Git_Automation
{
    meta:
        author = "migz-0day"
        description = "Detects git_to.py automated git add, commit, and push utility"
        repository = "https://github.com/migz-0day/script_vault"
        category = "developerTools"

    strings:
        $shebang = "#!/usr/bin/env python" ascii
        $subproc = "subprocess" ascii
        $os_sys = "os.system" ascii
        $git_add = "git add" ascii
        $git_commit = "git commit" ascii
        $git_push = "git push" ascii

    condition:
        filesize < 500KB and
        ($shebang or $subproc or $os_sys) and
        all of ($git_*)
}

rule ScriptVault_System_Info_Enumeration
{
    meta:
        author = "migz-0day"
        description = "Detects system.sh Linux distro, CPU, hostname, and disk enumeration script"
        repository = "https://github.com/migz-0day/script_vault"
        category = "systemAdmin"

    strings:
        $shebang1 = "#!/bin/bash" ascii
        $shebang2 = "#!/usr/bin/env bash" ascii
        $cmd_host = "hostname" ascii
        $cmd_cpu = "lscpu" ascii
        $proc_cpu = "/proc/cpuinfo" ascii
        $cmd_disk = "df -h" ascii
        $os_rel = "/etc/os-release" ascii
        $cmd_uname = "uname" ascii

    condition:
        filesize < 500KB and
        ($shebang1 or $shebang2) and
        3 of ($cmd_*, $proc_cpu, $os_rel)
}

rule ScriptVault_Node_Updater
{
    meta:
        author = "migz-0day"
        description = "Detects node_update.py Node.js installation and version management utility"
        repository = "https://github.com/migz-0day/script_vault"
        category = "systemAdmin"

    strings:
        $shebang = "#!/usr/bin/env python" ascii
        $node_str = "node" ascii nocase
        $nvm = "nvm" ascii nocase
        $npm = "npm" ascii nocase
        $ver_flag = "--version" ascii
        $subproc = "subprocess" ascii

    condition:
        filesize < 500KB and
        ($shebang or $subproc) and
        $node_str and
        any of ($nvm, $npm, $ver_flag)
}