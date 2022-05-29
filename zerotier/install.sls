{% if not salt['file.file_exists']('/usr/sbin/zerotier-one') %}
{{ tpldot }}.install:
  cmd.run:
    - name: |
       curl -s https://install.zerotier.com | bash
{% endif %}
