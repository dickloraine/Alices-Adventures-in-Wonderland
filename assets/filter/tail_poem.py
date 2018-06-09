import re
from textwrap import dedent
from panovel import run_pandoc_filter


def latex(self):
    return dedent(r"""
        \clearpage
        \begin{samepage}
        \settowidth{\versewidth}{a mouse that morning}
        \indentpattern{0135554322112346898779775545653222345544456688778899}
        \begin{verse}[\versewidth]
        \setlength{\vgap}{1em}
        \begin{patverse}
        \large Fury said to \\
        a mouse, That \\
        he met \\
        in the \\
        house, \\
        \normalsize `Let us \\
        both go \\
        to law: \\
        \emph{I} will \\
        prosecute \\
        \textit{you.} --- \\
        Come, I'll \\
        \small take no \\
        denial; \\
        We must \\
        have a \\
        trial: \\
        For \\
        \footnotesize really \\
        this \\
        morning \\
        I've \\
        nothing \\
        to do.' \\
        Said the \\
        mouse to \\
        \scriptsize the cur, \\
        Such a \\
        trial, \\
        dear sir, \\
        With no \\
        jury or \\
        judge, \\
        would be \\
        wasting \\
        our breath.' \\
        \tiny  `I'll be \\
        judge, \\
        I'll be \\
        jury.' \\
        Said \\
        cunning \\
        old Fury; \\
        `I'll try \\
        the whole \\
        cause \\
        and \\
        condemn \\
        you \\
        to \\
        death.'  \par
        \end{patverse}
        \end{verse}
        \end{samepage}
    """)


def html(self):
    return dedent("""
        <div id="tail">
            <p>&lsquo;Fury said to</p>
            <p class="tail2">a mouse, That</p>
            <p class="tail3">he met in the</p>
            <p class="tail4">house, &ldquo;Let</p>
            <p class="tail5">us both go</p>
            <div class="smaller">
            <p class="tail6">to law, <em>I</em></p>
            <p class="tail7">will prose-</p>
            <p class="tail8">cute <em>you</em>.&mdash;</p>
            <p class="tail7">Come, I’ll</p>
            <p class="tail6">take no de-</p>
            <div class="smaller">
                <p class="tail5">nial; We</p>
                <p class="tail4">must have</p>
                <p class="tail3">a trial:</p>
                <p class="tail2">For really</p>
                <p class="tail1">this morn-</p>
                <div class="smaller">
                <p class="tail2">ing I’ve</p>
                <p class="tail3">nothing</p>
                <p class="tail4">to do.&rdquo;</p>
                <p class="tail5">Said the</p>
                <p class="tail6">mouse to</p>
                <div class="smaller">
                    <p class="tail7">the cur,</p>
                    <p class="tail8">&ldquo;Such a</p>
                    <p class="tail7">trial, dear</p>
                    <p class="tail6">Sir, With</p>
                    <p class="tail5">no jury</p>
                    <div class="smaller">
                    <p class="tail4">or judge,</p>
                    <p class="tail3">would</p>
                    <p class="tail2">be wast-</p>
                    <p class="tail1">ing our</p>
                    <p class="tail2">breath.&rdquo;</p>
                    <div class="smaller">
                        <p class="tail3">&ldquo;I’ll be</p>
                        <p class="tail4">judge,</p>
                        <p class="tail5">I’ll be</p>
                        <p class="tail6">jury,&rdquo;</p>
                        <p class="tail7">Said</p>
                        <div class="smaller">
                        <p class="tail8">cun-</p>
                        <p class="tail7">ning</p>
                        <p class="tail6">old</p>
                        <p class="tail5">Fury:</p>
                        <p class="tail4">&ldquo;I’ll</p>
                        <div class="smaller">
                            <p class="tail3">try</p>
                            <p class="tail2">the</p>
                            <p class="tail1">whole</p>
                            <p class="tail2">cause</p>
                            <p class="tail3">and</p>
                            <div class="smaller">
                            <p class="tail4">con-</p>
                            <p class="tail5">demn</p>
                            <p class="tail6">you to</p>
                            <p class="tail7">death.&rdquo;&rsquo;</p>
                            </div>
                        </div>
                        </div>
                    </div>
                    </div>
                </div>
                </div>
            </div>
            </div>
        </div>
    """)


def other(self):
    new = ""
    for line in self.text.split("\n"):
        if line == "":
            new += '| ' + "\n"
        else:
            new += '| ' + line + "\n"
    new = re.sub(r'\|\s\|', '|', new, flags=re.MULTILINE)
    return new


if __name__ == "__main__":
    run_pandoc_filter(["tail_poem"], latex, html, other)
