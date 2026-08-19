def profile_car(manufacturer, model, **kwargs):
    kwargs['model'] = model
    kwargs['manufactor'] = manufacturer

    return kwargs
