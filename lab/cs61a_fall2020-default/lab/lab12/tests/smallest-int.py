test = {
  'name': 'smallest-int',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM smallest_int;
          11/13/2020 10:06:33|3
          11/13/2020 12:57:26|3
          11/13/2020 12:58:12|3
          11/13/2020 14:08:32|3
          11/13/2020 1:48:13|3
          11/13/2020 1:57:30|3
          11/13/2020 8:45:37|3
          11/13/2020 9:14:41|3
          11/13/2020 9:56:23|3
          11/13/2020 12:14:58|4
          11/13/2020 12:33:03|4
          11/13/2020 2:00:47|4
          11/13/2020 2:09:24|4
          11/13/2020 2:32:03|4
          11/13/2020 8:37:44|4
          11/13/2020 11:32:57|5
          11/13/2020 12:50:42|5
          11/13/2020 1:46:30|5
          11/13/2020 1:46:37|5
          11/13/2020 2:05:11|5
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab12.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
