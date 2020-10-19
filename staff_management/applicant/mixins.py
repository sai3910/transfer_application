class GroupRequiredMixin(object):
    """
        group_required - list of strings, required param
    """

    group_required = None

    def dispatch(self, request, *args, **kwargs):
        super_user = request.user.is_superuser  # noqa

        if not request.user.is_authenticated:
            raise PermissionDenied
        else:
            user_groups = []

            # check for user groups groups
            for group in request.user.groups.values_list('name', flat=True):
                user_groups.append(group)

            # check for module groups
            for group in request.user.module_groups.values_list('name', flat=True):
                user_groups.append(group)

            if len(set(user_groups).intersection(self.group_required)) <= 0 and not request.user.is_superuser:
                raise PermissionDenied

        return super(GroupRequiredMixin, self).dispatch(request, *args, **kwargs)