.. title: 配置 Zsh
.. slug: pei-zhi-zsh
.. date: 2020-01-14 19:22:50 UTC+08:00
.. tags: zsh
.. category:
.. link:
.. description:
.. type: text
.. has_math: true

.. include:: refs/aliases.ref

目前网络上推荐的 ZSH 扩展一般都是 `oh-my-zsh`_，但亲自使用一段时间后，发现 |a_OMZ| 有一个致命缺陷：

.. class:: zom-banner

    太慢了！

在网上阅读到了 `这篇文章 <https://www.aloxaf.com/2019/11/zplugin_tutorial/>`_，
得知了 Zsh 的一个更快速的插件管理器以及 『异步』 的命令提示符。

总之，编写 :code:`.zshrc` 脚本如下：

.. code:: zsh
    :number-lines:

    # LAST MOD: 2020-01-10
    # LESS COLOR
    export LESS_TERMCAP_mb=$(tput bold; tput setaf 2) # green
    export LESS_TERMCAP_md=$(tput bold; tput setaf 6) # cyan
    export LESS_TERMCAP_me=$(tput sgr0)
    export LESS_TERMCAP_so=$(tput bold; tput setaf 3; tput setab 4) # yellow on blue
    export LESS_TERMCAP_se=$(tput rmso; tput sgr0)
    export LESS_TERMCAP_us=$(tput smul; tput bold; tput setaf 7) # white
    export LESS_TERMCAP_ue=$(tput rmul; tput sgr0)
    export LESS_TERMCAP_mr=$(tput rev)
    export LESS_TERMCAP_mh=$(tput dim)
    export LESS_TERMCAP_ZN=$(tput ssubm)
    export LESS_TERMCAP_ZV=$(tput rsubm)
    export LESS_TERMCAP_ZO=$(tput ssupm)
    export LESS_TERMCAP_ZW=$(tput rsupm)

    # EDITOR
    export EDITOR='nvim'

    # RUST
    ## 更新 rust 工具链
    export RUSTUP_DIST_SERVER='https://mirrors.ustc.edu.cn/rust-static'
    ## 更新 rustup 本身
    export RUSTUP_UPDATE_ROOT='https://mirrors.tuna.tsinghua.edu.cn/rustup'

    [[ -d "$HOME/.local/bin" && "$PATH"==*"$HOME/.local/bin"* ]] && PATH="$PATH:$HOME/.local/bin"
    [[ -f "$HOME/.config/zsh/condainit.zsh" ]] && source "$HOME/.config/zsh/condainit.zsh"

    # 如果不是交互式就退出
    [[ $- != *i* ]] && return

    # ======>>>>>>>>>>> Interactive Shell Specification <<<<<<<<<<================
    ZPLUGIN_HOME="$HOME/.zplugin"
    # 检查 zplugin 是否安装
    if [ ! -f "$ZPLUGIN_HOME/bin/zplugin.zsh" ]; then
        echo "Install zplugin..."
        [ ! -d "$ZPLUGIN_HOME/bin" ] && mkdir -p "$ZPLUGIN_HOME/bin" 2> /dev/null
        URL="https://github.com/zdharma/zplugin.git"
        #URL="https://gitee.com/zombie110year/zplugin.git"
        git clone "$URL" "$ZPLUGIN_HOME/bin"
        echo "Zplugin install completed!"
    fi

    # 设置目录栈，用于快速跳转
    DIRSTACKSIZE=20
    setopt autopushd
    setopt pushdminus
    setopt pushdsilent
    setopt pushdtohome
    setopt pushdignoredups
    setopt cdablevars
    setopt interactivecomments      # 在交互式命令行中允许注释
    alias d='dirs -v | head -20'
    # 禁用纠错
    unsetopt correct_all
    unsetopt correct
    DISABLE_CORRECTION="true"
    # 启用 256 色终端
    export TERM="xterm-256color"
    # 如果是 WSL 则取消 BG_NICE
    [[ -d "/mnt/c" ]] && [[ "$(uname -a)" == *Microsoft* ]] && unsetopt BG_NICE
    # 在主题加载出错时提供一个默认 prompt
    export PS1="%n@%m:%~%# "
    # ==================== ZPLUGIN SPECIFICATION =================================
    source "$ZPLUGIN_HOME/bin/zplugin.zsh"
    ## ZSH 高亮
    ZSH_HIGHLIGHT_HIGHLIGHTERS=(main brackets pattern cursor root)
    #zplugin lightzsh-users/zsh-syntax-highlighting
    zplugin ice lucid wait='0' atinit='zpcompinit'
    zplugin light zdharma/fast-syntax-highlighting
    ## ZSH 补全
    zplugin ice lucid wait='0'
    zplugin light zsh-users/zsh-completions
    ## ZSH 自动建议
    ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE="fg=#ff00ff,bg=cyan,bold"
    ZSH_AUTOSUGGEST_USE_ASYNC=1
    zplugin ice wait='0' lucid atload '_zsh_autosuggest_start'
    zplugin light zsh-users/zsh-autosuggestions
    ## async theme
    zplugin ice pick"async.zsh" src"pure.zsh"
    zplugin light sindresorhus/pure

    # aliases
    alias ls='ls --color=auto'
    alias ll='ls -Al'
    export FZF_DEFAULT_COMMAND='fd --type f'

.. _`oh-my-zsh`: https://github.com/ohmyzsh/ohmyzsh
