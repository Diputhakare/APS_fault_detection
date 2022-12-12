from sensor.predictor import ModelResolver

model_resolver = ModelResolver()
model_resolver.get_latest_save_model_path()
model_resolver.get_latest_save_transformer_path()
model_resolver.get_latest_save_target_encoder_path()
model_resolver.get_latest_dir_path()