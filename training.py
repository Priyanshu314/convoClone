
from transformers import TrainingArguments, DataCollatorForSeq2Seq
from trl import SFTTrainer
from unsloth import is_bfloat16_supported
from data_preparation import load_and_prepare_data


def train_model(dataset, model, tokenizer, output_dir="outputs"):
    trainer = SFTTrainer(
        model=model,
        tokenizer=tokenizer,
        train_dataset=dataset,
        dataset_text_field="text",
        max_seq_length=2048,
        data_collator=DataCollatorForSeq2Seq(tokenizer=tokenizer),
        args=TrainingArguments(
            per_device_train_batch_size=2,
            gradient_accumulation_steps=4,
            warmup_steps=5,
            max_steps=60,
            learning_rate=2e-4,
            fp16=not is_bfloat16_supported(),
            bf16=is_bfloat16_supported(),
            logging_steps=1,
            optim="adamw_8bit",
            weight_decay=0.01,
            lr_scheduler_type="linear",
            seed=3407,
            output_dir=output_dir,
            report_to="none",
        )
    )
    trainer.train()
    trainer.save_model(output_dir)
    return trainer
