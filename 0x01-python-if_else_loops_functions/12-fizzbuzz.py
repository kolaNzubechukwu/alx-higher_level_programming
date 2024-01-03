{"payload":{"allShortcutsEnabled":false,"fileTree":{"0x01-python-if_else_loops_functions":{"items":[{"name":"0-positive_or_negative.py","path":"0x01-python-if_else_loops_functions/0-positive_or_negative.py","contentType":"file"},{"name":"1-last_digit.py","path":"0x01-python-if_else_loops_functions/1-last_digit.py","contentType":"file"},{"name":"10-add.py","path":"0x01-python-if_else_loops_functions/10-add.py","contentType":"file"},{"name":"10-main.py","path":"0x01-python-if_else_loops_functions/10-main.py","contentType":"file"},{"name":"100-print_tebahpla.py","path":"0x01-python-if_else_loops_functions/100-print_tebahpla.py","contentType":"file"},{"name":"101-main.py","path":"0x01-python-if_else_loops_functions/101-main.py","contentType":"file"},{"name":"101-remove_char_at.py","path":"0x01-python-if_else_loops_functions/101-remove_char_at.py","contentType":"file"},{"name":"102-magic_calculation.py","path":"0x01-python-if_else_loops_functions/102-magic_calculation.py","contentType":"file"},{"name":"11-main.py","path":"0x01-python-if_else_loops_functions/11-main.py","contentType":"file"},{"name":"11-pow.py","path":"0x01-python-if_else_loops_functions/11-pow.py","contentType":"file"},{"name":"12-fizzbuzz.py","path":"0x01-python-if_else_loops_functions/12-fizzbuzz.py","contentType":"file"},{"name":"12-main.py","path":"0x01-python-if_else_loops_functions/12-main.py","contentType":"file"},{"name":"13-insert_number.c","path":"0x01-python-if_else_loops_functions/13-insert_number.c","contentType":"file"},{"name":"2-print_alphabet.py","path":"0x01-python-if_else_loops_functions/2-print_alphabet.py","contentType":"file"},{"name":"3-print_alphabt.py","path":"0x01-python-if_else_loops_functions/3-print_alphabt.py","contentType":"file"},{"name":"4-print_hexa.py","path":"0x01-python-if_else_loops_functions/4-print_hexa.py","contentType":"file"},{"name":"5-print_comb2.py","path":"0x01-python-if_else_loops_functions/5-print_comb2.py","contentType":"file"},{"name":"6-print_comb3.py","path":"0x01-python-if_else_loops_functions/6-print_comb3.py","contentType":"file"},{"name":"7-islower.py","path":"0x01-python-if_else_loops_functions/7-islower.py","contentType":"file"},{"name":"7-main.py","path":"0x01-python-if_else_loops_functions/7-main.py","contentType":"file"},{"name":"8-main.py","path":"0x01-python-if_else_loops_functions/8-main.py","contentType":"file"},{"name":"8-uppercase.py","path":"0x01-python-if_else_loops_functions/8-uppercase.py","contentType":"file"},{"name":"9-main.py","path":"0x01-python-if_else_loops_functions/9-main.py","contentType":"file"},{"name":"9-print_last_digit.py","path":"0x01-python-if_else_loops_functions/9-print_last_digit.py","contentType":"file"},{"name":"README.md","path":"0x01-python-if_else_loops_functions/README.md","contentType":"file"},{"name":"linked_lists.c","path":"0x01-python-if_else_loops_functions/linked_lists.c","contentType":"file"},{"name":"lists.h","path":"0x01-python-if_else_loops_functions/lists.h","contentType":"file"}],"totalCount":27},"":{"items":[{"name":"0x00-python-hello_world","path":"0x00-python-hello_world","contentType":"directory"},{"name":"0x01-python-if_else_loops_functions","path":"0x01-python-if_else_loops_functions","contentType":"directory"},{"name":"0x02-python-import_modules","path":"0x02-python-import_modules","contentType":"directory"},{"name":"0x03-python-data_structures","path":"0x03-python-data_structures","contentType":"directory"},{"name":"0x04-python-more_data_structures","path":"0x04-python-more_data_structures","contentType":"directory"},{"name":"0x05-python-exceptions","path":"0x05-python-exceptions","contentType":"directory"},{"name":"0x06-python-classes","path":"0x06-python-classes","contentType":"directory"},{"name":"0x07-python-test_driven_development","path":"0x07-python-test_driven_development","contentType":"directory"},{"name":"0x08-python-more_classes","path":"0x08-python-more_classes","contentType":"directory"},{"name":"0x0A-python-inheritance","path":"0x0A-python-inheritance","contentType":"directory"},{"name":"0x0B-python-input_output","path":"0x0B-python-input_output","contentType":"directory"},{"name":"0x0C-python-almost_a_circle","path":"0x0C-python-almost_a_circle","contentType":"directory"},{"name":"0x0D-SQL_introduction","path":"0x0D-SQL_introduction","contentType":"directory"},{"name":"0x0E-SQL_more_queries","path":"0x0E-SQL_more_queries","contentType":"directory"},{"name":"0x10-python-network_0","path":"0x10-python-network_0","contentType":"directory"},{"name":"0x12-javascript-warm_up","path":"0x12-javascript-warm_up","contentType":"directory"},{"name":"0x13-javascript_objects_scopes_closures","path":"0x13-javascript_objects_scopes_closures","contentType":"directory"},{"name":"0x14-javascript-web_scraping","path":"0x14-javascript-web_scraping","contentType":"directory"},{"name":"0x1A-hash_tables","path":"0x1A-hash_tables","contentType":"directory"}],"totalCount":19}},"fileTreeProcessingTime":5.680987,"foldersToFetch":[],"reducedMotionEnabled":null,"repo":{"id":571760450,"defaultBranch":"master","name":"alx-higher_level_programming","ownerLogin":"NZUBE-ROOT","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2022-11-28T20:36:13.000Z","ownerAvatar":"https://avatars.githubusercontent.com/u/111927348?v=4","public":true,"private":false,"isOrgOwned":false},"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"master","listCacheKey":"v0:1669669803.5502641","canEdit":false,"refType":"branch","currentOid":"82ccd684d49b73245802c74589889c9c50425ee0"},"path":"0x01-python-if_else_loops_functions/12-fizzbuzz.py","currentUser":null,"blob":{"rawLines":["#!/usr/bin/python3","def fizzbuzz():","    for num in range(1, 101):","        if (num % 3 == 0 and num % 5 == 0):","            print('FizzBuzz', end=' ')","        elif num % 5 == 0:","            print('Buzz', end=' ')","        elif num % 3 == 0:","            print('Fizz', end=' ')","        else:","            print('{}'.format(num), end=' ')"],"stylingDirectives":[[{"start":0,"end":18,"cssClass":"pl-c"}],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":12,"cssClass":"pl-en"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":11,"cssClass":"pl-s1"},{"start":12,"end":14,"cssClass":"pl-c1"},{"start":15,"end":20,"cssClass":"pl-en"},{"start":21,"end":22,"cssClass":"pl-c1"},{"start":24,"end":27,"cssClass":"pl-c1"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":12,"end":15,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":22,"cssClass":"pl-c1"},{"start":23,"end":24,"cssClass":"pl-c1"},{"start":25,"end":28,"cssClass":"pl-c1"},{"start":29,"end":32,"cssClass":"pl-s1"},{"start":33,"end":34,"cssClass":"pl-c1"},{"start":35,"end":36,"cssClass":"pl-c1"},{"start":37,"end":39,"cssClass":"pl-c1"},{"start":40,"end":41,"cssClass":"pl-c1"}],[{"start":12,"end":17,"cssClass":"pl-en"},{"start":18,"end":28,"cssClass":"pl-s"},{"start":30,"end":33,"cssClass":"pl-s1"},{"start":33,"end":34,"cssClass":"pl-c1"},{"start":34,"end":37,"cssClass":"pl-s"}],[{"start":8,"end":12,"cssClass":"pl-k"},{"start":13,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":21,"end":23,"cssClass":"pl-c1"},{"start":24,"end":25,"cssClass":"pl-c1"}],[{"start":12,"end":17,"cssClass":"pl-en"},{"start":18,"end":24,"cssClass":"pl-s"},{"start":26,"end":29,"cssClass":"pl-s1"},{"start":29,"end":30,"cssClass":"pl-c1"},{"start":30,"end":33,"cssClass":"pl-s"}],[{"start":8,"end":12,"cssClass":"pl-k"},{"start":13,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":21,"end":23,"cssClass":"pl-c1"},{"start":24,"end":25,"cssClass":"pl-c1"}],[{"start":12,"end":17,"cssClass":"pl-en"},{"start":18,"end":24,"cssClass":"pl-s"},{"start":26,"end":29,"cssClass":"pl-s1"},{"start":29,"end":30,"cssClass":"pl-c1"},{"start":30,"end":33,"cssClass":"pl-s"}],[{"start":8,"end":12,"cssClass":"pl-k"}],[{"start":12,"end":17,"cssClass":"pl-en"},{"start":18,"end":22,"cssClass":"pl-s"},{"start":23,"end":29,"cssClass":"pl-en"},{"start":30,"end":33,"cssClass":"pl-s1"},{"start":36,"end":39,"cssClass":"pl-s1"},{"start":39,"end":40,"cssClass":"pl-c1"},{"start":40,"end":43,"cssClass":"pl-s"}]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/NZUBE-ROOT/alx-higher_level_programming/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":null,"repoAlertsPath":"/NZUBE-ROOT/alx-higher_level_programming/security/dependabot","repoSecurityAndAnalysisPath":"/NZUBE-ROOT/alx-higher_level_programming/settings/security_analysis","repoOwnerIsOrg":false,"currentUserCanAdminRepo":false},"displayName":"12-fizzbuzz.py","displayUrl":"https://github.com/NZUBE-ROOT/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/12-fizzbuzz.py?raw=true","headerInfo":{"blobSize":"331 Bytes","deleteInfo":{"deleteTooltip":"You must be signed in to make or propose changes"},"editInfo":{"editTooltip":"You must be signed in to make or propose changes"},"ghDesktopPath":"https://desktop.github.com","gitLfsPath":null,"onBranch":true,"shortPath":"ba6d5de","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2FNZUBE-ROOT%2Falx-higher_level_programming%2Fblob%2Fmaster%2F0x01-python-if_else_loops_functions%2F12-fizzbuzz.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"11","truncatedSloc":"11"},"mode":"executable file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"loggedIn":false,"newDiscussionPath":"/NZUBE-ROOT/alx-higher_level_programming/discussions/new","newIssuePath":"/NZUBE-ROOT/alx-higher_level_programming/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/NZUBE-ROOT/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/12-fizzbuzz.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","dismissStackNoticePath":"/settings/dismiss-notice/publish_stack_from_file","releasePath":"/NZUBE-ROOT/alx-higher_level_programming/releases/new?marketplace=true","showPublishActionBanner":false,"showPublishStackBanner":false},"rawBlobUrl":"https://github.com/NZUBE-ROOT/alx-higher_level_programming/raw/master/0x01-python-if_else_loops_functions/12-fizzbuzz.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"NZUBE-ROOT","repoName":"alx-higher_level_programming","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":false,"actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timed_out":false,"not_analyzed":false,"symbols":[{"name":"fizzbuzz","kind":"function","ident_start":23,"ident_end":31,"extent_start":19,"extent_end":330,"fully_qualified_name":"fizzbuzz","ident_utf16":{"start":{"line_number":1,"utf16_col":4},"end":{"line_number":1,"utf16_col":12}},"extent_utf16":{"start":{"line_number":1,"utf16_col":0},"end":{"line_number":10,"utf16_col":44}}}]}},"copilotInfo":null,"copilotAccessAllowed":false,"csrf_tokens":{"/NZUBE-ROOT/alx-higher_level_programming/branches":{"post":"Zbs8_TDiplJrlNyi_wsh9slSNWnL7-HoqyiZozaYOxECLaT22ysjr9SP3hvybNEsh3xF-8STP38gng4CA9Cieg"},"/repos/preferences":{"post":"qCR10Wp2edl91rWukMY6UnLvEGttfXKel4h3wDtzV5yg8Ip0EwF14qLjZb0HzEnUCFkbfb3hxrZ0G8yQ673ZoA"}}},"title":"alx-higher_level_programming/0x01-python-if_else_loops_functions/12-fizzbuzz.py at master · NZUBE-ROOT/alx-higher_level_programming"}