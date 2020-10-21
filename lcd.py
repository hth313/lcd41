class Ann(object):
    def __init__(self, name, padding = 0):
        self.value = False
        self.name  = name
        self.width = len(name) + padding
        self.empty = " " * self.width
    def set(self):
        self.value = True
    def reset(self):
        self.value = False
    def text(self):
        if self.value:
            return self.name.ljust(self.width)
        else:
            return self.empty

class Anns(object):
    def __init__(self):
        self.annBAT   = Ann("BAT", 3)
        self.annUSER  = Ann("USER", 3)
        self.annG     = Ann("G")
        self.annRAD   = Ann("RAD", 3)
        self.annSHIFT = Ann("SHIFT", 3)
        self.ann0     = Ann("O")
        self.ann1     = Ann("1")
        self.ann2     = Ann("2")
        self.ann3     = Ann("3")
        self.ann4     = Ann("4", 3)
        self.annPRGM  = Ann("PRGM", 3)
        self.annALPHA = Ann("ALPHA")
    def text(self):
        return self.annBAT.text() + self.annUSER.text() + self.annG.text() +        \
            self.annRAD.text() + self.annSHIFT.text() + self.ann0.text() +   \
            self.ann1.text() + self.ann2.text() + self.ann3.text() +         \
            self.ann4.text() + self.annPRGM.text() + self.annALPHA.text()

class LCD41(object):
    def __init__(self):
        pass
    def image(self, text = "", anns = Anns()):
        return '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   width="68mm"
   height="13mm"
   viewBox="0 0 68 13"
   version="1.1"
   id="svg8"
   inkscape:version="1.0rc1 (09960d6, 2020-04-09)"
   sodipodi:docname="lcd.svg">
  <defs
     id="defs2">
    <rect
       id="rect8277"
       height="4.2763124"
       width="2.0045214"
       y="45.034915"
       x="31.003265" />
  </defs>
  <sodipodi:namedview
     id="base"
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1.0"
     inkscape:pageopacity="0.0"
     inkscape:pageshadow="2"
     inkscape:zoom="1.979899"
     inkscape:cx="107.93637"
     inkscape:cy="173.03661"
     inkscape:document-units="mm"
     inkscape:current-layer="layer1"
     inkscape:document-rotation="0"
     showgrid="false"
     inkscape:window-width="1252"
     inkscape:window-height="855"
     inkscape:window-x="80"
     inkscape:window-y="23"
     inkscape:window-maximized="0" />
  <metadata
     id="metadata5">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
        <dc:title />
      </cc:Work>
    </rdf:RDF>
  </metadata>
  <g
     inkscape:label="Layer 1"
     inkscape:groupmode="layer"
     id="layer1"
     style="display:inline">
    <rect
       style="fill:#000000;stroke-width:0.264583"
       id="rect7372"
       width="68"
       height="13"
       x="0"
       y="0"
       ry="0" />
    <rect
       style="fill:#dbf0cb;stroke-width:0.264583;fill-opacity:1"
       id="rect7374"
       width="66"
       height="11"
       x="1"
       y="1"
       rx="1"
       ry="1"
       sodipodi:insensitive="true" />
    <text
       id="text8269"
       y="9.413212"
       x="4.067822"
       style="font-size:2.11667px;line-height:1.25;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Normal';stroke-width:0.264583"
       xml:space="preserve"><tspan
         style="stroke-width:0.264583"
         y="9.413212"
         x="4.067822"
         id="tspan8267"
         sodipodi:role="line" /></text>
    <text
       id="text8273"
       y="11.417732"
       x="2.063301"
       style="font-size:2.21667px;line-height:1.25;font-family:'Andale Mono';-inkscape-font-specification:'Andale Mono, Normal';inline-size:64.1291;stroke-width:0.264583"
       xml:space="preserve"><tspan
         sodipodi:role="line"
         x="2.063301"
         y="11.417732"><tspan
           style="stroke-width:0.264583">{annunciators}</tspan></tspan></text>
    <text
       style="line-height:1.25;font-family:sans-serif;font-size:3.88055555999999990px;-inkscape-font-specification:'sans-serif, Normal';white-space:pre;shape-inside:url(#rect8277);"
       id="text8275"
       xml:space="preserve" />
    <text
       id="text8283"
       y="7.542324"
       x="2.5"
       style="font-size:6.08px;line-height:1.25;font-family:'HP41 Character Set Xtended';-inkscape-font-specification:'HP41 Character Set Xtended';stroke-width:0.264583"
       xml:space="preserve"><tspan
         style="stroke-width:0.264583"
         y="7.542324"
         x="2.5"
         id="tspan8281"
         sodipodi:role="line">{text}</tspan></text>
  </g>
</svg>
'''.format(text=text, annunciators=anns.text())
