"""Default instructions for different annotation protocols."""

# Default instructions for each protocol
# These are used when no custom instructions are provided
PROTOCOL_INSTRUCTIONS = {
    "DA": """
        <ul>
          <li>Score each translation using the slider based on meaning preservation and quality.
            <strong>Important:</strong> The relative order of scores matters; ensure better translations have higher
            scores than worse ones.
            <ul>
              <li>0: <strong>Nonsense</strong>: most information is lost.</li>
              <li>33%: <strong>Broken</strong>: major gaps and narrative issues.</li>
              <li>66%: <strong>Middling</strong>: minor issues with grammar or consistency.</li>
              <li>100%: <strong>Perfect</strong>: meaning and grammar align completely with the source.</li>
            </ul>
          </li>
        </ul>
    """,
    "ESA": """
        <ul>
          <li>Error spans:
            <ul>
              <li><strong>Click</strong> on the start of an error, then <strong>click</strong> on the end to mark an
                error span.</li>
              <li><strong>Hover</strong> over an existing highlight to change error severity (minor/major) or remove it.
              </li>
            </ul>
            Error severity:
            <ul>
              <li><span class="instruction_sev" id="instruction_sev_minor">Minor:</span> Style, grammar, or word choice
                could be better.</li>
              <li><span class="instruction_sev" id="instruction_sev_major">Major:</span> Meaning is significantly
                changed or is hard to understand.</li>
            </ul>
            <strong>Tip</strong>: Mark the general area of the error (doesn't need to be exact). Use separate highlights
            for different errors.
            Use <code>[missing]</code> at the end of a sentence for omitted content.<br>
          </li>
          <li>Score each translation using the slider based on meaning preservation and quality.
            <strong>Important:</strong> The relative order of scores matters; ensure better translations have higher
            scores than worse ones.
            <ul>
              <li>0: <strong>Nonsense</strong>: most information is lost.</li>
              <li>33%: <strong>Broken</strong>: major gaps and narrative issues.</li>
              <li>66%: <strong>Middling</strong>: minor issues with grammar or consistency.</li>
              <li>100%: <strong>Perfect</strong>: meaning and grammar align completely with the source.</li>
            </ul>
          </li>
        </ul>
    """,
    "MQM": """
        <ul>
          <li>Error spans:
            <ul>
              <li><strong>Click</strong> on the start of an error, then <strong>click</strong> on the end to mark an
                error span.</li>
              <li><strong>Hover</strong> over an existing highlight to change error severity (minor/major) or remove it.
              </li>
            </ul>
            Error severity:
            <ul>
              <li><span class="instruction_sev" id="instruction_sev_minor">Minor:</span> Style, grammar, or word choice
                could be better.</li>
              <li><span class="instruction_sev" id="instruction_sev_major">Major:</span> Meaning is significantly
                changed or is hard to understand.</li>
            </ul>
            <strong>Tip</strong>: Mark the general area of the error (doesn't need to be exact). Use separate highlights
            for different errors.
            Use <code>[missing]</code> at the end of a sentence for omitted content.<br>
          </li>
          <li>Score each translation using the slider based on meaning preservation and quality.
            <strong>Important:</strong> The relative order of scores matters; ensure better translations have higher
            scores than worse ones.
            <ul>
              <li>0: <strong>Nonsense</strong>: most information is lost.</li>
              <li>33%: <strong>Broken</strong>: major gaps and narrative issues.</li>
              <li>66%: <strong>Middling</strong>: minor issues with grammar or consistency.</li>
              <li>100%: <strong>Perfect</strong>: meaning and grammar align completely with the source.</li>
            </ul>
          </li>
          <li>
            Error types:
            After highlighting an error fragment, you will be asked to select the specific error type (main category and
            subcategory).
            If you are unsure about which errors fall under which categories, please consult the <a
              href="https://themqm.org/the-mqm-typology/"
              style="font-weight: bold; text-decoration: none; color: black;">typology
              definitions</a>.
          </li>
        </ul>
    """,

    "STEL": """
        <ul>

          <strong>Technical instructions:</strong>
          <ul>
            <li><strong>Click</strong> on the start of an error, then <strong>click</strong> on the end to mark an
              error span.</li>
            <li><strong>Hover</strong> over an existing highlight to change error category (Critical/Major/Negligible/Redundancy) or remove it.
            </li>
            <li> Mark the general area of the error (doesn't need to be exact). Use separate highlights for different errors.
            Use <code>[missing]</code> at the end of a sentence for omitted content.
            </li>
            <li>Additionally, score each translation using the slider based on meaning preservation and quality.
            <strong>Important:</strong> The relative order of scores matters; ensure better translations have higher
            scores than worse ones.
            <ul>
              <li>0: <strong>Nonsense</strong>: most information is lost.</li>
              <li>33%: <strong>Broken</strong>: major gaps and narrative issues.</li>
              <li>66%: <strong>Middling</strong>: minor issues with grammar or consistency.</li>
              <li>100%: <strong>Perfect</strong>: meaning and grammar align completely with the source.</li>
            </ul>
            </li>
          </ul>

          Assumptions:
          <ul>
            <li>
            Assume the communication situation of the event where this document was recorded. Assume a communication goal, typical audience, 
            and their background knowledge. Assume there is a speech-to-text interpreter producing this content, and the audience at the event follows it. 
            If not specified otherwise, assume it is a live event, speaker and audience are in the same room, and the translations are presentented to the 
            audience in real-time on a big screen in the room.
            </li>
            <li>
            The primary focus of this annotation is adequacy: preservation of meaning that supports communication goal. 
            Primary focus is not fluency: grammar, syntax, order of words and clauses, etc.
            </li>
            <li>
            Take into consideration other instructions of your manager (or the person who assigned you this task). 
            From time constraints, there may be need to highlight only critical or minor errors, and leave the other umarked because highlighting 
            all of them would create little benefits for much labour. 
            </li>
          </ul>

          Label severities of errors:
          <ul>
            <li><span class="instruction_sev" id="instruction_sev_major">Critical:</span> an error that misleads the audience into false beliefs or assumptions, 
            from which they can not recover by themselves.</li>
            <li><span class="instruction_sev" id="instruction_sev_minor">Minor:</span> an error that affects meaning but the audience can recognize and correct 
            by themselves from their background knowledge, from listening to the source language, from provided meta-information, etc.</li>
            <li><span class="instruction_sev" id="instruction_sev_neutral">Negligible:</span> a small error that does not affect meaning and audience can easily 
            overlook it. E.g. minor grammal or style flaw, use of inappropriate but not confusing synonym, inconsitency, etc.</li>
            <li><span class="instruction_sev" id="instruction_sev_redundancy">Redundancy:</span> not an error but redundant content that should rather be
            removed because it could annoy or distract the audience. E.g. filler words, hessitation, false starts, repetition, unintended remark, etc.
          </ul>

          Two additional labels:
          <ul>
            <li><span class="instruction_sev" id="instruction_sev_embarrassing">"and embarrassing"</span> is for critical errors that have potential 
            of creating an immediate negative effect at the communication event, such as embarrassing or offending speaker or audience, 
            or cause laughter when it is not appropriate.
            <li><span class="instruction_sev" id="instruction_sev_redundancy">"and redundancy":</span> if the text span is redundant information, 
            and an error as well, highlight it as critical/minor/negligible, and add a label "and redundancy".</li>
            <li><span class="instruction_sev" id="instruction_sev_neutral">- , which means "none":</span> nothing else to add.
            </li> 
          </ul>
        </ul>
    """,

}
