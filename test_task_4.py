import re
import task_4


PatternAndReplacement = tuple[str, str]
InputAndOutput = tuple[str, str]
TestCase = tuple[PatternAndReplacement, list[InputAndOutput]]

tests: list[TestCase] = [
    (
        task_4.REGEXP_1,
        [
            ("aAc", "a!A!c"),
            ("aZc", "a!Z!c"),
            ("aZZc", "a!Z!!Z!c"),
            ("aBaCa", "a!B!a!C!a"),
        ],
    ),
    (
        task_4.REGEXP_2,
        [
            ("abc", "abc"),
            ("abbc", "abc"),
            ("azzzc", "azc"),
            ("arrrrc", "arc"),
            ("xxxxxx", "x"),
        ],
    ),
    (
        task_4.REGEXP_3,
        [
            ("this is text", "this is text"),
            ("this is is text", "this *is* text"),
            ("this is is is text", "this *is* text"),
            ("this is text text", "this is *text*"),
            ("this is is text text", "this *is* *text*"),
        ],
    ),
    (
        task_4.REGEXP_4,
        [
            ("one two three", "two one three"),
            ("dog cat wolf", "cat dog wolf"),
            ("goose car rat", "goose rat car"),
        ],
    ),
    # (
    #     task_4.REGEXP_5,
    #     [
    #         ("cat dog", "cat dog"),
    #         ("cat dog cat", "cat dog cat"),
    #         ("dog cat dog cat cat", "dog dog"),
    #         ("dog cat dog rat rat cat cat", "dog dog rat rat"),
    #     ],
    # ),
]


def test_task_4():
    for (pattern, repl), cases in tests:
        regexp = re.compile(pattern)

        for string, expected in cases:
            actual = regexp.sub(repl, string)
            assert actual == expected
