#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
print("NOTYET, 20250213 To be soted out.")
sys.exit()


"""\
*    *[Summary]* :: An =ICM=: a beginning template for development of new ICMs.
"""

####+BEGIN: bx:cs:python:top-of-file :partof "bystar" :copyleft "halaal+minimal"
""" #+begin_org
*  This file:/bisos/git/bxRepos/bisos-pip/githubApi/py3/bin/githubApiReports.py :: [[elisp:(org-cycle)][| ]]
 is part of The Libre-Halaal ByStar Digital Ecosystem. http://www.by-star.net
 *CopyLeft*  This Software is a Libre-Halaal Poly-Existential. See http://www.freeprotocols.org
 A Python Interactively Command Module (PyICM).
 Best Developed With COMEEGA-Emacs And Best Used With Blee-ICM-Players.
 *WARNING*: All edits wityhin Dynamic Blocks may be lost.
#+end_org """
####+END:

"""
*  [[elisp:(org-cycle)][| *ICM-INFO:* |]] :: Author, Copyleft and Version Information
"""
####+BEGIN: bx:cs:python:name :style "fileName"
__icmName__ = "githubApiReports"
####+END:

####+BEGIN: bx:global:timestamp:version-py :style "date"
__version__ = "201811303009"
####+END:

####+BEGIN: bx:global:icm:status-py :status "Production"
__status__ = "Production"
####+END:

__credits__ = [""]

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/csInfo-mbNedaGpl.py"
csInfo = {
    'authors':         ["[[http://mohsen.1.banan.byname.net][Mohsen Banan]]"],
    'copyright':       "Copyright 2017, [[http://www.neda.com][Neda Communications, Inc.]]",
    'licenses':        ["[[https://www.gnu.org/licenses/agpl-3.0.en.html][Affero GPL]]", "Libre-Halaal Services License", "Neda Commercial License"],
    'maintainers':     ["[[http://mohsen.1.banan.byname.net][Mohsen Banan]]",],
    'contacts':        ["[[http://mohsen.1.banan.byname.net/contact]]",],
    'partOf':          ["[[http://www.by-star.net][Libre-Halaal ByStar Digital Ecosystem]]",]
}
####+END:

####+BEGIN: bx:cs:python:topControls :partof "bystar" :copyleft "halaal+minimal"
"""
*  [[elisp:(org-cycle)][|/Controls/| ]] :: [[elisp:(org-show-subtree)][|=]]  [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[file:Panel.org][Panel]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(delete-other-windows)][(1)]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]
"""
####+END:

####+BEGIN: bx:cs:python:section :title "ContentsList"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ContentsList*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:cs:python:icmItem :itemType "=Imports=" :itemTitle "*IMPORTS*"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  =Imports=      :: *IMPORTS*  [[elisp:(org-cycle)][| ]]
"""
####+END:

####+BEGIN: b:py3:cs:framework/imports :basedOn "classification"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] *Imports* =Based on Classification=cs-mu=
#+end_org """
from bisos import b
from bisos.b import cs
from bisos.b import b_io
from bisos.common import csParam

import collections
####+END:

import sys
#import os

from bisos.csPlayer import bleep

# import os
# import sys
# import subprocess
# import traceback
# import time
# import string
# import random
# import requests
# import uuid
# import datetime
import pprint

from bisos.githubApi import githubApiLib

g_importedCmnds = {        # Enumerate modules from which CMNDs become invokable
    'bleep': bleep.__file__,
    'githubApiLib': githubApiLib.__file__,    
}
    

####+BEGIN: bx:cs:python:section :title "= =Framework::= ICM  Description (Overview) ="
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= ICM  Description (Overview) =*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "icmOverview" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 3 :pyInv ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  ICM-Cmnd       :: /icmOverview/ parsMand= parsOpt= argsMin=0 argsMax=3 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class icmOverview(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 3,}

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if rtInv.outs:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {}
        if not cs.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:

        moduleDescription="""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Description:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Xref]          :: *[Related/Xrefs:]*  <<Xref-Here->>  -- External Documents  [[elisp:(org-cycle)][| ]]

**  [[elisp:(org-cycle)][| ]]   Model and Terminology                                      :Overview:
*** bxpRootXxFile   -- /etc/bystarRoot, ~/.bystarRoot, /bystar
*** bxpRoot         -- Base For This Module
*** bpb             -- ByStar Platform Base, Location Of Relevant Parts (Bisos, blee, bsip
*** bpd             -- ByStar Platform Directory (Object), An instance of Class BxpBaseDir
**      [End-Of-Description]
"""
        
        moduleUsage="""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Usage:* | ]]

**      How-Tos:
**      [End-Of-Usage]
"""
        
        moduleStatus="""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Status:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Info]          :: *[Current-Info:]* Status/Maintenance -- General TODO List [[elisp:(org-cycle)][| ]]
** TODO [[elisp:(org-cycle)][| ]]  Current         :: Just getting started [[elisp:(org-cycle)][| ]]
**      [End-Of-Status]
"""
        
####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/moduleOverview.py"
        icm.unusedSuppressForEval(moduleUsage, moduleStatus)
        actions = self.cmndArgsGet("0&2", cmndArgsSpecDict, argsList)
        if actions[0] == "all":
            cmndArgsSpec = cmndArgsSpecDict.argPositionFind("0&2")
            argChoices = cmndArgsSpec.argChoicesGet()
            argChoices.pop(0)
            actions = argChoices
        for each in actions:
            print(each)
            if rtInv.outs:
                #print( str( __doc__ ) )  # This is the Summary: from the top doc-string
                #version(interactive=True)
                exec("""print({})""".format(each))
                
        return(format(str(__doc__)+moduleDescription))

    """
**  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(org-tree-to-indirect-buffer)][|>]] [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(beginning-of-buffer)][Top]] [[elisp:(delete-other-windows)][(1)]] || Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&2",
            argName="actions",
            argDefault='all',
            argChoices=['all', 'moduleDescription', 'moduleUsage', 'moduleStatus'],
            argDescription="Output relevant information",
        )

        return cmndArgsSpecDict
####+END:


####+BEGIN: bx:cs:python:section :title "= =Framework::= ICM Hooks ="
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= ICM Hooks =*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:cs:python:func :funcName "g_icmChars" :comment "ICM Characteristics Spec" :funcType "FrameWrk" :retType "Void" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-FrameWrk  :: /g_icmChars/ =ICM Characteristics Spec= retType=Void argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def g_icmChars():
####+END:
    csInfo['panel'] = "{}-Panel.org".format(__icmName__)
    csInfo['groupingType'] = "IcmGroupingType-pkged"
    csInfo['cmndParts'] = "IcmCmndParts[common] IcmCmndParts[param]"
    
g_icmChars()


####+BEGIN: bx:cs:python:func :funcName "g_icmPreCmnds" :funcType "FrameWrk" :retType "Void" :deco "default" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-FrameWrk  :: /g_icmPreCmnds/ retType=Void argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def g_icmPreCmnds():
####+END:
    """ PreHook """
    pass


####+BEGIN: bx:cs:python:func :funcName "g_icmPostCmnds" :funcType "FrameWrk" :retType "Void" :deco "default" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-FrameWrk  :: /g_icmPostCmnds/ retType=Void argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
@io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
def g_icmPostCmnds():
####+END:
    """ PostHook """
    pass


####+BEGIN: bx:cs:python:section :title "= =Framework::= Options, Arguments and Examples Specifications ="
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= Options, Arguments and Examples Specifications =*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: bx:cs:python:func :funcName "g_argsExtraSpecify" :comment "FrameWrk: ArgsSpec" :funcType "FrameWrk" :retType "Void" :deco "" :argsList "parser"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-FrameWrk  :: /g_argsExtraSpecify/ =FrameWrk: ArgsSpec= retType=Void argsList=(parser)  [[elisp:(org-cycle)][| ]]
"""
def g_argsExtraSpecify(
    parser,
):
####+END:
    """Module Specific Command Line Parameters.
    g_argsExtraSpecify is passed to G_main and is executed before argsSetup (can not be decorated)
    """
    G = cs.globalContext.get()
    csParams = cs.CmndParamDict()

    csParams.parDictAdd(
        parName='moduleVersion',
        parDescription="Module Version",
        parDataType=None,
        parDefault=None,
        parChoices=list(),
        parScope=icm.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--version',
    )

    csParams.parDictAdd(
        parName='reportFormat',
        parDescription="Format Of Report -- latex, org-mode, etc",
        parDataType=None,
        parDefault='latex',
        parChoices=list(),
        parScope=icm.CmndParamScope.TargetParam,
        argparseShortOpt=None,
        argparseLongOpt='--reportFormat',
    )

    bleep.commonParamsSpecify(csParams)    
       
    cs.argsparseBasedOnCsParams(parser, csParams)

    # So that it can be processed later as well.
    G.icmParamDictSet(csParams)
    
    return


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "examples" :cmndType "ICM-Cmnd-FWrk" :comment "FrameWrk: ICM Examples" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  ICM-Cmnd-FWrk  :: /examples/ =FrameWrk: ICM Examples= parsMand= parsOpt= argsMin=0 argsMax=0 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class examples(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
    ):
        cmndOutcome = self.getOpOutcome()
        if rtInv.outs:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome

        callParamsDict = {}
        if not cs.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome

####+END:
        def cpsInit(): return collections.OrderedDict()
        def menuItem(verbosity): cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity=verbosity)
        def execLineEx(cmndStr): cs.examples.execInsert(execLine=cmndStr)

        logControler = b_io.log.Control()
        logControler.loggerSetLevel(20)
        
        cs.examples.myName(cs.G.icmMyName(), cs.G.icmMyFullName())
        
        cs.examples.commonBrief()

        bleep.examples_csBasic()

        apiUrl_reposOfUser = "https://api.github.com/users/mohsenBanan/repos"
        apiUrl_orgsOfUser = "https://api.github.com/users/mohsenBanan/orgs"
        apiUrl_oneOrg = "https://api.github.com/orgs/ByStar"
        apiUrl_oneRepo = "https://api.github.com/repos/mohsenBanan/ReposOverview"                      

####+BEGIN: bx:cs:python:cmnd:subSection :title "Github Api Access"
        """
**  [[elisp:(beginning-of-buffer)][Top]] ============== [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *Github Api Access*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
        githubApiLib.examples_githubApiAccess()

####+BEGIN: bx:cs:python:cmnd:subSection :title "Github Repos Of Orgs Of Users Reports"
        """
**  [[elisp:(beginning-of-buffer)][Top]] ============== [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *Github Repos Of Orgs Of Users Reports*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
        cs.examples.menuChapter('*Github Repos Of Orgs Of Users Reports*')

        cmndName = "reposOfOrgsOfUsersReport"
        cmndArgs = apiUrl_orgsOfUser
        cps = cpsInit(); cps["reportFormat"] = "latex"
        menuItem(verbosity='none')
        
####+BEGIN: bx:cs:python:cmnd:subSection :title "Github Repos Of Orgs Reports"
        """
**  [[elisp:(beginning-of-buffer)][Top]] ============== [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *Github Reports*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
        cs.examples.menuChapter('*Github Repos Of Orgs Reports*')

        cmndName = "reposOfOrgsReport"
        cmndArgs = apiUrl_oneOrg
        cps = cpsInit(); cps["reportFormat"] = "latex"
        menuItem(verbosity='none')
        
####+BEGIN: bx:cs:python:cmnd:subSection :title "Github Repos Reports"
        """
**  [[elisp:(beginning-of-buffer)][Top]] ============== [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *Github Repos Reports*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
        cs.examples.menuChapter('*Github Repos Of Orgs Reports*')

        cmndName = "reposReport"
        cmndArgs = apiUrl_oneRepo
        cps = cpsInit(); cps["reportFormat"] = "latex"
        menuItem(verbosity='none')

####+BEGIN: bx:cs:python:cmnd:subSection :title "Pipeline Examples"
        """
**  [[elisp:(beginning-of-buffer)][Top]] ============== [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *Pipeline Examples*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
        cs.examples.menuChapter('*Combined Pipeline Example*')

        execLineEx("""cp /dev/null githubReport.tex""")
        thisFile = __file__
        #thisFile = __main__.__file__
        execLineEx("""{thisFile} -i listOrgsOfUsers {apiUrl_orgsOfUser} | xargs -n  3 {thisFile2} -i reposOfOrgsReport |  tee -a githubReport.tex"""
                   .format(
                       thisFile=thisFile,
                       apiUrl_orgsOfUser=apiUrl_orgsOfUser,
                       thisFile2=thisFile,
                   )
        )
         
        
#####+BEGIN: bx:cs:python:cmnd:subSection :title "Remain In Sycn With Template"
        """
**  [[elisp:(beginning-of-buffer)][Top]] ============== [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]          *Remain In Sycn With Template*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
#####+END:
        
#         cs.examples.menuChapter('*Remain In Sycn With Template*')

#         #templateFile = "/de/bx/nne/dev-py/pypi/pkgs/bisos/examples/dev/bin/icmBegin.py"
#         templateFile = "/de/bx/nne/dev-py/pypi/pkgs/uni sos/icmExamples/dev/bin/icmBegin.py"
#         thisFile = __file__

#         execLineEx("""diff {thisFile} {templateFile}""".format(thisFile=thisFile, templateFile=templateFile))
#         execLineEx("""cp {thisFile} {templateFile}""".format(thisFile=thisFile, templateFile=templateFile))
#         execLineEx("""cp {templateFile} {thisFile}""".format(thisFile=thisFile, templateFile=templateFile))                

        return(cmndOutcome)

    def cmndDocStr(self): return """
** ICM Examples -- List of commonly used lines for this ICM [[elisp:(org-cycle)][| ]]
"""
    
   
    
####+BEGIN: bx:dblock:global:file-insert :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/G_examples.bottom.py"
    # Intentionally Left Blank -- previously: lhip.G_devExamples(G_myName)

####+END:


####+BEGIN: bx:cs:python:section :title "ICM Commands"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ICM Commands*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "reposOfOrgsOfUsersReport" :comment "" :parsMand "" :parsOpt "reportFormat" :argsMin 0 :argsMax 9999 :pyInv ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  ICM-Cmnd       :: /reposOfOrgsOfUsersReport/ parsMand= parsOpt=reportFormat argsMin=0 argsMax=9999 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class reposOfOrgsOfUsersReport(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'reportFormat', ]
    cmndArgsLen = {'Min': 0, 'Max': 9999,}

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        reportFormat=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if rtInv.outs:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {'reportFormat': reportFormat, }
        if not cs.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        reportFormat = callParamsDict['reportFormat']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        cmndArgs = self.cmndArgsGet("0&9999", cmndArgsSpecDict, argsList)

        opResults = {}

        outcome = githubApiLib.listOrgsOfUsers().cmnd(
            interactive=False,
            argsList=cmndArgs,
        ).log()
        if outcome.isProblematic(): return(io.eh.badOutcome(outcome))

        orgsOfUsers = outcome.results

        if not orgsOfUsers:
            return(io.eh.badOutcome(outcome))

        for userUrl, orgsOfThisUser in orgsOfUsers.items():
            for eachOrg in orgsOfThisUser:
                #pprint.pprint(eachOrg)                
                reportProduce_org(eachOrg, reportFormat)
                apiUrlOfOrg = eachOrg["url"]
                outcome = githubApiLib.listReposOfOrgs().cmnd(
                    interactive=False,
                    argsList=[apiUrlOfOrg],
                ).log()
                if outcome.isProblematic(): return(io.eh.badOutcome(outcome))

                reposOfOrgs = outcome.results

                if not reposOfOrgs:
                    continue
                                                 
                for apiUrlOfOrg, reposOfThisOrg in reposOfOrgs.items():
                    for eachRepo in reposOfThisOrg:
                        apiUrlOfRepo = eachRepo["url"]
                        outcome = githubApiLib.reposInfo().cmnd(
                            interactive=False,
                            argsList=[apiUrlOfRepo],
                        ).log()
                        if outcome.isProblematic(): return(io.eh.badOutcome(outcome))

                        reposInfo = outcome.results

                        if not reposInfo:
                            continue
                        
                        for apiUrlOfRepo, infoForThisRepo in reposInfo.items():
                            reportProduce_repo(infoForThisRepo, reportFormat) 

        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=opResults,
        )

####+BEGIN: b:py3:cs:method/typing :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:        
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&9999",
            argName="cmndArgs",
            argChoices=[],
            argDescription="Exec all or those specified as functions.",
        )

        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:method/typing :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndDocStr/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(self):
####+END:        
        return """
***** TODO [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Place holder for this commands doc string.
"""


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "reposOfOrgsReport" :comment "" :parsMand "" :parsOpt "reportFormat" :argsMin 0 :argsMax 9999 :pyInv ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  ICM-Cmnd       :: /reposOfOrgsReport/ parsMand= parsOpt=reportFormat argsMin=0 argsMax=9999 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class reposOfOrgsReport(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'reportFormat', ]
    cmndArgsLen = {'Min': 0, 'Max': 9999,}

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        reportFormat=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if rtInv.outs:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {'reportFormat': reportFormat, }
        if not cs.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        reportFormat = callParamsDict['reportFormat']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        cmndArgs = self.cmndArgsGet("0&9999", cmndArgsSpecDict, argsList)

        opResults = {}

        for eachOrgUrl in cmndArgs:
            outcome = githubApiLib.orgsInfo().cmnd(
                interactive=False,
                argsList=[eachOrgUrl],
            ).log()
            if outcome.isProblematic(): return(io.eh.badOutcome(outcome))

            orgsInfoDict = outcome.results

            orgInfo = orgsInfoDict[eachOrgUrl]
            
            reportProduce_org(orgInfo, reportFormat)

            outcome = githubApiLib.listReposOfOrgs().cmnd(
                interactive=False,
                argsList=[eachOrgUrl],
            ).log()
            if outcome.isProblematic(): return(io.eh.badOutcome(outcome))

            reposOfOrgs = outcome.results

            if not reposOfOrgs:
                return(io.eh.badOutcome(outcome))            

            for apiUrlOfOrg, reposOfThisOrg in reposOfOrgs.items():
                for eachRepo in reposOfThisOrg:
                    apiUrlOfRepo = eachRepo["url"]
                    outcome = githubApiLib.reposInfo().cmnd(
                        interactive=False,
                        argsList=[apiUrlOfRepo],
                    ).log()
                    if outcome.isProblematic(): return(io.eh.badOutcome(outcome))

                    reposInfo = outcome.results

                    if not reposInfo:
                        continue

                    for apiUrlOfRepo, infoForThisRepo in reposInfo.items():
                        reportProduce_repo(infoForThisRepo, reportFormat) 

        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=opResults,
        )

####+BEGIN: b:py3:cs:method/typing :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:        
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&9999",
            argName="cmndArgs",
            argChoices=[],
            argDescription="Exec all or those specified as functions.",
        )

        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:method/typing :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndDocStr/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(self):
####+END:        
        return """
***** TODO [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Place holder for this commands doc string.
"""

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "reposReport" :comment "" :parsMand "" :parsOpt "reportFormat" :argsMin 0 :argsMax 9999 :pyInv ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  ICM-Cmnd       :: /reposReport/ parsMand= parsOpt=reportFormat argsMin=0 argsMax=9999 asFunc= interactive=  [[elisp:(org-cycle)][| ]]
"""
class reposReport(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'reportFormat', ]
    cmndArgsLen = {'Min': 0, 'Max': 9999,}

    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
        interactive=False,        # Can also be called non-interactively
        reportFormat=None,         # or Cmnd-Input
        argsList=[],         # or Args-Input
    ):
        cmndOutcome = self.getOpOutcome()
        if rtInv.outs:
            if not self.cmndLineValidate(outcome=cmndOutcome):
                return cmndOutcome
            effectiveArgsList = G.icmRunArgsGet().cmndArgs
        else:
            effectiveArgsList = argsList

        callParamsDict = {'reportFormat': reportFormat, }
        if not cs.cmndCallParamsValidate(callParamsDict, interactive, outcome=cmndOutcome):
            return cmndOutcome
        reportFormat = callParamsDict['reportFormat']

        cmndArgsSpecDict = self.cmndArgsSpec()
        if not self.cmndArgsValidate(effectiveArgsList, cmndArgsSpecDict, outcome=cmndOutcome):
            return cmndOutcome
####+END:
        cmndArgs = self.cmndArgsGet("0&9999", cmndArgsSpecDict, argsList)

        opResults = {}

        outcome = githubApiLib.reposInfo().cmnd(
            interactive=False,
            argsList=cmndArgs,
        ).log()
        if outcome.isProblematic(): return(io.eh.badOutcome(outcome))

        reposInfo = outcome.results

        if not reposInfo:
            return(io.eh.badOutcome(outcome))            

        for apiUrlOfRepo, infoForThisRepo in reposInfo.items():
            reportProduce_repo(infoForThisRepo, reportFormat) 

        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=opResults,
        )

####+BEGIN: b:py3:cs:method/typing :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndArgsSpec/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
####+END:        
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&9999",
            argName="cmndArgs",
            argChoices=[],
            argDescription="Exec all or those specified as functions.",
        )

        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:method/typing :methodName "cmndDocStr" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList ""
    """
**  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Method-anyOrNone :: /cmndDocStr/ retType=bool argsList=nil deco=default  [[elisp:(org-cycle)][| ]]
"""
    @io.track.subjectToTracking(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndDocStr(self):
####+END:        
        return """
***** TODO [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Place holder for this commands doc string.
"""


####+BEGIN: bx:cs:python:section :title "Supporting Classes And Functions"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Supporting Classes And Functions*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:cs:python:func :funcName "reportProduce_org" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "orgInfo reportFormat"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-anyOrNone :: /reportProduce_org/ retType=bool argsList=(orgInfo reportFormat)  [[elisp:(org-cycle)][| ]]
"""
def reportProduce_org(
    orgInfo,
    reportFormat,
):
####+END:
   orgName = orgInfo['login']
   description = orgInfo['description']
   if not description:
       description = "Empty-At-This-Time"
   
   orgUrl = orgInfo['html_url']

   #pprint.pprint(orgInfo)
   
   print((
       """\
\subsection{{Organization: {orgName}}}

\\url{{{orgUrl}}}

Github Organization Description: {description}
"""
       .format(
           orgName=orgName,
           description=description,
           orgUrl=orgUrl,
       )
   ))
   

####+BEGIN: bx:cs:python:func :funcName "reportProduce_repo" :funcType "anyOrNone" :retType "bool" :deco "" :argsList "repoInfo reportFormat"
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-anyOrNone :: /reportProduce_repo/ retType=bool argsList=(repoInfo reportFormat)  [[elisp:(org-cycle)][| ]]
"""
def reportProduce_repo(
    repoInfo,
    reportFormat,
):
####+END:
   repoName = repoInfo['name']   # eg overview
   repoOrg = repoInfo['organization']['login']
   description = repoInfo['description']
   if not description:
       description = "Empty-For-Now"

   ssh_url = repoInfo['ssh_url']
   html_url = repoInfo['html_url']
   git_url = repoInfo['git_url']   

   print((
       """\
\subsubsection{{Repository: {repoOrg}/{repoName}}}

SSH Url:  \\url{{{ssh_url}}}\\\\
HTML Url: \\url{{{html_url}}}\\\\
GIT Url:  \\url{{{git_url}}}\\\\


Repository Description: {description}
"""
       .format(
           repoOrg=repoOrg,
           repoName=repoName,
           ssh_url=ssh_url,
           html_url=html_url,
           git_url=git_url,                      
           description=description,
       )
   ))


####+BEGIN: bx:cs:python:section :title "Common/Generic Facilities -- Library Candidates"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Common/Generic Facilities -- Library Candidates*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
"""
*       /Empty/  [[elisp:(org-cycle)][| ]]
"""

       
####+BEGIN: bx:cs:python:section :title "= =Framework::=   G_main -- Instead Of ICM Dispatcher ="
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::=   G_main -- Instead Of ICM Dispatcher =*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:cs:python:func :funcName "G_main" :funcType "FrameWrk" :retType "Void" :deco "" :argsList ""
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Func-FrameWrk  :: /G_main/ retType=Void argsList=nil  [[elisp:(org-cycle)][| ]]
"""
def G_main():
####+END:
    """ 
** Replaces ICM dispatcher for other command line args parsings.
"""
    pass

####+BEGIN: bx:cs:python:icmItem :itemType "Configuration" :itemTitle "= =Framework::= g_ Settings -- ICMs Imports ="
"""
*  [[elisp:(org-cycle)][| ]] [[elisp:(org-show-subtree)][|=]] [[elisp:(show-children 10)][|V]] [[elisp:(bx:orgm:indirectBufOther)][|>]] [[elisp:(bx:orgm:indirectBufMain)][|I]] [[elisp:(blee:ppmm:org-mode-toggle)][|N]] [[elisp:(org-top-overview)][|O]] [[elisp:(progn (org-shifttab) (org-content))][|C]] [[elisp:(delete-other-windows)][|1]]  Configuration  :: = =Framework::= g_ Settings -- ICMs Imports =  [[elisp:(org-cycle)][| ]]
"""
####+END:

g_examples = examples  # or None
g_mainEntry = None  # or G_main

####+BEGIN: bx:dblock:global:file-insert :file "/libre/ByStar/InitialTemplates/update/sw/icm/py/icm2.G_main.py"
"""
*  [[elisp:(beginning-of-buffer)][Top]] # /Dblk-Begin/ # [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= ICM main() =*
"""

def classedCmndsDict():
    """
** Should be done here, can not be done in icm library because of the evals.
"""
    callDict = dict()
    for eachCmnd in icm.cmndList_mainsMethods().cmnd(
            interactive=False,
            importedCmnds=g_importedCmnds,
            mainFileName=__file__,
    ):
        try:
            callDict[eachCmnd] = eval("{}".format(eachCmnd))
            continue
        except NameError:
            pass

        for mod in g_importedCmnds:
            try:
                eval("{mod}.{cmnd}".format(mod=mod, cmnd=eachCmnd))
            except AttributeError:
                continue
            try:                
                callDict[eachCmnd] = eval("{mod}.{cmnd}".format(mod=mod, cmnd=eachCmnd))
                break
            except NameError:
                pass
    return callDict

csInfo['icmName'] = __icmName__
csInfo['version'] = __version__
csInfo['status'] = __status__
csInfo['credits'] = __credits__

G = cs.globalContext.get()
G.csInfo = csInfo

def g_icmMain():
    """This ICM's specific information is passed to G_mainWithClass"""
    sys.exit(
        icm.G_mainWithClass(
            inArgv=sys.argv[1:],                 # Mandatory
            extraArgs=g_argsExtraSpecify,        # Mandatory
            G_examples=g_examples,               # Mandatory            
            classedCmndsDict=classedCmndsDict(),   # Mandatory
            mainEntry=g_mainEntry,
            g_icmPreCmnds=g_icmPreCmnds,
            g_icmPostCmnds=g_icmPostCmnds,
        )
    )

g_icmMain()

"""
*  [[elisp:(beginning-of-buffer)][Top]] ## /Dblk-End/ ## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *= =Framework::= ICM main() =*
"""

####+END:

####+BEGIN: bx:cs:python:section :title "Unused Facilities -- Temporary Junk Yard"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *Unused Facilities -- Temporary Junk Yard*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:
"""
*       /Empty/  [[elisp:(org-cycle)][| ]]
"""

####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :title " ~End Of Editable Text~ "
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *End Of Editable Text*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]] 
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/libre/ByStar/InitialTemplates/software/plusOrg/dblock/inserts/endOfFileControls.org"
#+STARTUP: showall
####+END:
